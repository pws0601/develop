import pymongo

conn = pymongo.MongoClient('mongodb://10.10.224.3',10127)
db = conn['taDB']
coll = db['userDic']

docs = coll.find(
    {
        '$or' : [
            {'status' : 'I'},
            {'status' : 'U'}
        ]
    }
    )

dicDataList = list()
for doc in docs:
    dicDataList.append(doc)

spacePattern = '[- ]?'

userDicList = list()

for dicData in dicDataList:
    category = dicData['category']
    # 검출 방법 및 대표 키워드 & 키워드 리스트
    representative_word = ''
    words = list()
    positive_patterns = ''
    nagative_patterns = ''

    words_ = dicData['words']
    for word_ in words_:
        print('word_ : ',word_)
        word = word_['word']
        representative = word_['representative']
        if representative :
            representative_word = word
        words.append(word)
    
    ## Center
    center_words = list()
    center_patterns = list()
    if 'center' in dicData:
        centerDict = dicData['center']
        if 'words' in centerDict:
            center_words = centerDict['words']
        if 'patterns' in centerDict:
            center_patterns = centerDict['patterns']
    
    ## Left
    left_inclusion = bool()
    left_words = list()
    left_patterns = list()
    if 'left' in dicData:        
        leftDict = dicData['left']
        left_inclusion = leftDict['inclusion']
        if 'words' in leftDict:
            left_words = leftDict['words']
        if 'patterns' in leftDict:
            left_patterns = leftDict['patterns']
    for left_word in left_words:
        for center_word in center_words:
            add_word = left_word+spacePattern+center_word
            if left_inclusion : 
                positive_patterns = positive_patterns + add_word + '|'
            else :
                nagative_patterns = nagative_patterns + add_word + '|'
    for left_pattern in left_patterns:
        for center_pattern in center_patterns:
            add_pattern = left_pattern+center_pattern
            if left_inclusion :
                positive_patterns = positive_patterns + add_pattern + "|"
            else : 
                nagative_patterns = nagative_patterns + add_pattern + "|"

    ## Right
    right_inclusion = bool()
    right_words = list()
    right_patterns = list()
    if 'right' in dicData:
        rightDict = dicData['right']
        right_inclusion = rightDict['inclusion']
        if 'words' in rightDict:
            right_words = rightDict['words']
        if 'patterns' in rightDict:
            right_patterns = rightDict['patterns']
    
    for center_word in center_words:
        for right_word in right_words:
            add_word = center_word + spacePattern + right_word
            if right_inclusion : 
                positive_patterns = positive_patterns + add_pattern + "|"
            else : 
                nagative_patterns = nagative_patterns + add_pattern + "|"
    
    for center_pattern in center_patterns:
        for right_pattern in right_patterns:
            add_pattern = center_pattern + right_pattern
            if right_inclusion:
                positive_patterns = positive_patterns + add_pattern + "|"
            else : 
                nagative_patterns = nagative_patterns + add_pattern + "|"
    
    userDict = dict()
    userDict['representative_word'] = representative_word
    userDict['words'] = words
    userDict['positive_patterns'] = positive_patterns
    userDict['nagative_patterns'] = nagative_patterns
    userDicList.append(userDict)


import json


res = json.dumps(userDicList,ensure_ascii=False)


import redis
import datetime

# redis 연결

rd = redis.StrictRedis(host='localhost', port=6379, db=0)

rd.set("userDict",res,datetime.timedelta(seconds=60))



