import ray

ray.init()

@ray.remote
class Actor:
    async def heavy_compute(self):
        print("HEAVY_COMPUTE")
        return

# Actor 객체 생성도 .remote()를 활용
actor = Actor.remote()

NUM_TASKS = 100000
result_refs = []

for _ in range(NUM_TASKS):
    print(_)
    result_refs.append(actor.heavy_compute.remote())

ray.get(result_refs)
