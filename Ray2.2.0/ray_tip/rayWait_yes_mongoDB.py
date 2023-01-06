import ray
import pymongo

@ray.remote
def posAnalysis(num,data):
    sentence = data['sentence']
    tokens = ''
    data['tokens'] = tokens
    return (num, data)

conn = pymongo.MongoClient('mongodb://10.10.224.3',10127)
db = conn['taDB']
coll = db['preProcessCollection_22002']
query = dict()
query['call_id'] = '22002_20220916143931_42810'
callData = coll.find_one(query)
dataList = callData['data']
dataList = dataList + dataList
ray.init()
MAX_NUM_PENDING_TASKS = 10
result_refs = []

for i in range(len(dataList)):
    if len(result_refs) > MAX_NUM_PENDING_TASKS:
        ready_refs, result_refs = ray.wait(result_refs, num_returns=1)
        for num, data in ray.get(ready_refs):
            dataList[num] = data        
    result_refs.append(
        posAnalysis.remote(i,dataList[i])
    )
for num, data in ray.get(result_refs):
            dataList[num] = data        

for data in dataList:
    print(data)

conn.close()



