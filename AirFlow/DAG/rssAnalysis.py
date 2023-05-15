import airflow
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

import os
import re
import pandas as pd
from time import mktime
from datetime import datetime
import hashlib
import pymongo
from aiohttp import ClientSession
import json
from pymongo.errors import OperationFailure
import asyncio


savePath = "/tmp/rssDir/newsAnalysis/"+str(datetime.today().strftime('%Y%m%d'))
saveFilePath = savePath+"/targetDatas.csv"
resultFilePath = savePath+"/resultDatas.csv"

#mongoDB replicaSet 접속 설정
replica_set = "10.10.224.58:10071,10.10.224.58:10072,10.10.224.58:10073"
uri = f"mongodb://{replica_set}/?replicaSet=rs0"

def makeKey(basekey:str):
    key = basekey.encode('UTF-8')
    enc = hashlib.md5()
    enc.update(key)
    return enc.hexdigest()

def makeSaveDir():
    os.makedirs(savePath,exist_ok=True)

def saveDataFile(saveFilePath:str,saveList:list):
     df = pd.DataFrame(saveList)
     df.to_csv(saveFilePath, header=False, index=False)

def getTargetData():
    conn = pymongo.MongoClient(uri)
    db = conn['xtrmSMA']
    coll = db['NEWS_ORIGIN']
    saveList = list(coll.find({'status':False}))
    saveDataFile(saveFilePath,saveList)
    conn.close


async def pos_str(sentences, kind_of_tagger='utagger'):
    pos_url = 'http://10.10.224.58:10042/morphologicalAnalysis'
    headers = {'Content-type': 'application/json'}
    data = {'text': sentences, 'tagger': kind_of_tagger, 'type': 'line', 'withEng': False}
    pos = ''
    async with ClientSession() as session:
        async with session.post(pos_url,headers=headers,json=data) as response:
            if response.status == 200:
                result = await response.text()                
                result = json.loads(result)
                if len(result['result']) != 0:
                    pos = result['result'][0]
    return pos


from kiwipiepy import Kiwi
kiwi = Kiwi()
async def sentenceSplit(sentence:str)->list() :
    try:    
        sentences = list()
        tokenized_sentence_list = kiwi.split_into_sents(sentence)
        for tokenized_sentence in tokenized_sentence_list:
            tmp_sentence = tokenized_sentence[0]
            if len(tmp_sentence) > 0 :
                sentences.append(tmp_sentence)
    except Exception as e:
        print(e)
        return []
    return sentences


async def targetDataAnalysis():
    targetDataList = pd.read_csv(saveFilePath, header=None).values.tolist()
    resultDataList = list()
    conn = pymongo.MongoClient(uri)
    db = conn['xtrmSMA']
    coll = db['NEWS_ORIGIN']
    with conn.start_session() as session:
        try:
            with session.start_transaction():
                for targetDatas in targetDataList:
                    orignDataDict = dict()
                    orignDataDict['_id']        = targetDatas[0]
                    orignDataDict['newsId']     = targetDatas[1]
                    orignDataDict['url']        = targetDatas[2]
                    orignDataDict['category']   = targetDatas[3]
                    orignDataDict['press']      = targetDatas[4]
                    orignDataDict['regDate']    = targetDatas[5]
                    orignDataDict['author']     = targetDatas[6]
                    orignDataDict['content']    = targetDatas[7]
                    orignDataDict['title']      = targetDatas[8]
                    orignDataDict['status']     = targetDatas[9]
                    titles = await sentenceSplit(targetDatas[8])
                    contents = await sentenceSplit(targetDatas[7])
                    titleTokens = ''
                    contentTokens = ''
                    if len(titles)>0 :
                        titleTokens = await asyncio.wait_for(pos_str(titles), timeout=5)
                    if len(contents)>0 :                     
                        contentTokens = await asyncio.wait_for(pos_str(contents), timeout=5)

                    orignDataDict['titleTokens']      = titleTokens
                    orignDataDict['contentTokens']     = contentTokens
                    resultDataList.append(orignDataDict)
                    coll.update_one(
                        {
                            '_id':orignDataDict['_id']
                        }, { "$set" : 
                            {
                                'status':True
                            }
                        }                        
                    )
            session.commit_transaction()
            saveDataFile(saveFilePath=resultFilePath, saveList=resultDataList)
        except OperationFailure as e:
            session.abort_transaction()
    conn.close()

def insertMongoDBTransaction():
    insertData = pd.read_csv(resultFilePath, header=None).values.tolist()
    conn = pymongo.MongoClient(uri)
    db = conn['xtrmSMA']
    coll = db['NEWS_ANALYSIS']
    with conn.start_session() as session:
        try:
            with session.start_transaction():
                for data in insertData:
                    orignDataDict = dict()
                    orignDataDict['_id']        = data[0]
                    orignDataDict['newsId']     = data[1]
                    orignDataDict['url']        = data[2]
                    orignDataDict['category']   = data[3]
                    orignDataDict['press']      = data[4]
                    orignDataDict['regDate']    = data[5]
                    orignDataDict['author']     = data[6]
                    orignDataDict['content']    = data[7]
                    orignDataDict['title']      = data[8]
                    orignDataDict['status']     = data[9]
                    orignDataDict['titleTokens']      = data[10]
                    orignDataDict['contentTokens']     = data[11]
                    doc = coll.find_one({'_id':orignDataDict['_id']}, session=session)
                    if doc is None:
                        coll.insert_one(orignDataDict)
                    else : 
                        continue
                    
            session.commit_transaction()
        except OperationFailure as e:
            session.abort_transaction()
    conn.close()


def coroutine_task():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(targetDataAnalysis())
    loop.close()



dag=DAG( # 객체의 인스턴스 생성(구체화) - 모든 워크플로의 시작점
    dag_id="rssAnalysis", # DAG 이름
    start_date=airflow.utils.dates.days_ago(1), # DAG 처음 실행 시작 날짜
    #schedule_interval=None, # DAG 실행 간격
    schedule_interval="@hourly",
)


make_save_dir=PythonOperator( # 파일 저장 경로 생성
    task_id="make_save_dir", # 태스크 이름
    python_callable=makeSaveDir,
    dag=dag,
)

get_target_data=PythonOperator( # 처리할 데이터 가져오기
    task_id="get_target_data", # 태스크 이름
    python_callable=getTargetData,
    dag=dag,
)

target_data_analysis=PythonOperator( # 처리할 데이터 형태소 분석
    task_id="target_data_analysis", # 태스크 이름
    python_callable=coroutine_task,
    dag=dag,
)

insert_transaction=PythonOperator( # 형태소분석된 데이터 처리(트랜잭션)
    task_id="insert_transaction", # 태스크 이름
    python_callable=insertMongoDBTransaction,
    dag=dag,
)

make_save_dir >> get_target_data >> target_data_analysis >> insert_transaction # 태스크 실행 순서 설정