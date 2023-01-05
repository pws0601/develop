import ray

ray.init()

@ray.remote
class Actor:
    async def heavy_compute(self):
        #print("HEAVY_COMPUTE")
        return

# Actor 객체 생성도 .remote()를 활용
actor = Actor.remote()

NUM_TASKS = 100000
MAX_NUM_PENDING_TASKS = 100

result_refs = []
for _ in range(NUM_TASKS):
    if len(result_refs) > MAX_NUM_PENDING_TASKS:
        ready_refs, result_refs = ray.wait(result_refs, num_returns=1)
        print(_ ," : ", len(result_refs))
        ray.get(ready_refs)
    result_refs.append(actor.heavy_compute.remote())
ray.get(result_refs)