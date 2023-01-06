import ray

ray.init()

@ray.remote
class Actor:
    async def heavy_compute(self,num):
        #print("HEAVY_COMPUTE")
        return str(num)+"번째 작업"

# Actor 객체 생성도 .remote()를 활용
actor = Actor.remote()

NUM_TASKS = 10
MAX_NUM_PENDING_TASKS = 2
result_list = list()
result_refs = []
for _ in range(NUM_TASKS):
    if len(result_refs) > MAX_NUM_PENDING_TASKS:
        ready_refs, result_refs = ray.wait(result_refs, num_returns=1)        
        result_list.append(ray.get(ready_refs))        
    result_refs.append(actor.heavy_compute.remote(_))
    print(result_refs)
result_list = result_list + ray.get(result_refs)
print(result_list)