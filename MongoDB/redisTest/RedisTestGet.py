import redis
import json

# redis 연결
rd = redis.StrictRedis(host='172.17.0.4', port=6379, db=0)

byteUserDict = rd.get("userDict")
userDictList = byteUserDict.decode('utf-8')
userDictList = json.loads(userDictList)
print(type(userDictList))
for userDict in userDictList:    
    print('representative_word : ', userDict['representative_word'] )
    print('positive_patterns": : ', userDict['positive_patterns'] )
    print('nagative_patterns": : ', userDict['nagative_patterns'] )
