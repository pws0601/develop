import airflow
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

import os
import re
import ssl
import pandas as pd
import feedparser
import requests
from goose3 import Goose
from goose3.text import StopWordsKorean
import urllib3
from time import mktime
from datetime import datetime
import hashlib
import pymongo
from pymongo.errors import OperationFailure

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# rss 수집 대상 리스트 파일
rssFilePath = '/home/ta/project/dataAnalysis/document/rss/2.csv'
# 수집 데이터 자정 경로
savePath = "/tmp/rssDir/news/"+str(datetime.today().strftime('%Y%m%d'))
saveFilePath = savePath+"/press2.csv"

#mongoDB replicaSet 접속 설정
replica_set = "10.10.224.58:10071,10.10.224.58:10072,10.10.224.58:10073"
uri = f"mongodb://{replica_set}/?replicaSet=rs0"


def makeKey(basekey:str):
    key = basekey.encode('UTF-8')
    enc = hashlib.md5()
    enc.update(key)
    return enc.hexdigest()


def cleanhtml(raw_html:str):
  raw_html = raw_html.replace('&gt;','<').replace('&lt;','>')
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


def get_data(url,encode):
    try:
        res = requests.get(url,verify=False)        
        res.encoding=encode
        html = res.text
        data = feedparser.parse(html)
        return data
    except Exception as e:        
        return None

def makeSaveDir():
    os.makedirs(savePath,exist_ok=True)

def saveDataFile(saveFilePath:str,saveList:list):
     df = pd.DataFrame(saveList)
     df.to_csv(saveFilePath, header=False, index=False)
    
def getContentGoose3(link:str)->str:
    # 본문데이터 파싱
    try:
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        reader = Goose({
            'stopwords_class':StopWordsKorean,
            'ssl_verify_hostname' : False,
            'ssl_context' : context,
            'timeout' : 30,
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
            })                
        contents = reader.extract(url=link)
        content = contents.cleaned_text
        return content
    except Exception as e:
        return ""



def rssCrawler() -> list :
    df = pd.read_csv(rssFilePath, header=None)
    
    saveList = list()
    if os.path.isfile(saveFilePath) : 
        saveList = pd.read_csv(saveFilePath, header=None).values.tolist()
    
    for rssData in df.values.tolist():    
        press = rssData[0]
        category = rssData[1]
        url = rssData[2]
        encode = rssData[3]
        parsed_data = get_data(url,encode)        
        for article in parsed_data['entries']:
            try:
                author = ''
                if 'author' in article:
                    author = article['author']            
                title = article['title']            
                summary = cleanhtml(article['summary'])        
                regDate = article['published_parsed']
                regDate = str(datetime.fromtimestamp(mktime(regDate)))
                link = article['link']
                primaryKey = makeKey(link+regDate)
                newsId = makeKey(link)
                content = getContentGoose3(link)
                if len(content) == 0 :             
                    content = summary
                if len(summary) == 0 and 'content' in article:
                    content = cleanhtml(article['content'][0]['value'])                
                if str(saveList).find(primaryKey) == -1:
                    orignDataDict = dict()
                    orignDataDict['_id'] = primaryKey
                    orignDataDict['newsId'] = newsId
                    orignDataDict['url'] = link
                    orignDataDict['category'] = category
                    orignDataDict['press'] = press
                    orignDataDict['regDate'] = regDate
                    orignDataDict['author'] = author
                    orignDataDict['content'] = content
                    orignDataDict['title'] = title
                    orignDataDict['status'] = True
                    saveList.append(orignDataDict)
            except Exception as e:
                print('error = ',e)
                print('article link :: ',article['link'])    
    saveDataFile(saveFilePath, saveList)
    

def insertMongoDBTransaction(insertData:list):
    conn = pymongo.MongoClient(uri)
    db = conn['xtrmSMA']
    coll = db['NEWS_ORIGIN']
    with conn.start_session() as session:
        try:
            with session.start_transaction():
                for data in insertData:
                    doc = coll.find_one({'_id':data['_id']}, session=session)
                    if doc is None:
                        coll.insert_one(data)
                    else : 
                        continue
            session.commit_transaction()
        except OperationFailure as e:
            session.abort_transaction()
    conn.close()


def insertDataMart():
    rssDataList = pd.read_csv(saveFilePath, header=None).values.tolist()
    insertList = list()
    saveList = list()
    for i in range(len(rssDataList)):
        rssData = rssDataList[i]
        orignDataDict = dict()
        orignDataDict['_id']        = rssData[0]
        orignDataDict['newsId']     = rssData[1]
        orignDataDict['url']        = rssData[2]
        orignDataDict['category']   = rssData[3]
        orignDataDict['press']      = rssData[4]
        orignDataDict['regDate']    = rssData[5]
        orignDataDict['author']     = rssData[6]
        orignDataDict['content']    = rssData[7]
        orignDataDict['title']      = rssData[8]        
        if rssData[9] :             
            insertList.append(orignDataDict)
        orignDataDict['status']      = False        
        saveList.append(orignDataDict)
    
    if len(insertList) > 0:
        insertMongoDBTransaction(insertList)
    saveDataFile(saveFilePath=saveFilePath, saveList=saveList)

dag=DAG( # 객체의 인스턴스 생성(구체화) - 모든 워크플로의 시작점
    dag_id="rssCrawler_news_2", # DAG 이름
    start_date=airflow.utils.dates.days_ago(1), # DAG 처음 실행 시작 날짜
    schedule_interval="@daily", # DAG 실행 간격
)

make_save_dir=PythonOperator( # BashOperator를 이용해 curl로 URL 결과값 다운로드
    task_id="make_save_dir", # 태스크 이름
    python_callable=makeSaveDir,
    dag=dag,
)

rss_crawler=PythonOperator( # DAG에서 pythonOperator를 사용하여 파이썬 함수 호출
    task_id="rss_crawler",
    python_callable=rssCrawler,
    dag=dag,
)

insert_data_mart=PythonOperator(
    task_id="insert_data_mart",                                         
    python_callable=insertDataMart,
    dag=dag,
)

make_save_dir >> rss_crawler >> insert_data_mart # 태스크 실행 순서 설정


