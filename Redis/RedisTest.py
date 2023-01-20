import redis
conn = redis.StrictRedis(host='172.17.0.4', port=6379, db=0)
#print(conn.keys())
#print(conn.hkeys('compoundDict_D002'))
#conn.delete('compoundDict_D002','*')
#conn.hdel('compoundDict_D002','*')
#print(conn.keys())

print(conn.hkeys('compoundDict_D002'))


#print(conn.flushall())
#print(conn.hget('compoundDict_D002','배달/NNG 의/JKG 민족/NNG'))
"""
target = '배달/NNG 의/JKG 민족/NNG'
replace = '배달의민족/NNG'

posResult = "안녕하/VA 세요/EF 배달/NNG 의/JKG 민족/NNG 상담원/NNG 이/VCP ㅂ니다/EF 무엇/NP 을/JKO 돕/VV 아/EC 드리/VX ㄹ까/EF 요/JX"

count = 6

detectectedPosList = list()

targetList = posResult.split(' ')
for count in range(count+1,1,-1):
    for i in range(len(targetList)):
        startIndex = i
        endIndex = i+count
        if endIndex == len(targetList) :
            break
        else : 
            targetStr = ' '.join(map(str, targetList[i:endIndex]))
            if targetStr == target:
                detectDict = dict()
                detectDict['target'] = target
                detectDict['replace'] = replace
                detectectedPosList.append(detectDict)

print(posResult)
for detectDict in detectectedPosList:
    posResult = posResult.replace(detectDict['target'],detectDict['replace'])
print(posResult)
"""