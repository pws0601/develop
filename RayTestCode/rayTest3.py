import numpy as np
import ray

ray.init(num_cpus=8)

arr = np.random.random(1000000)

@ray.remote
def mul(x):
    return x * 10

arr = ray.put(arr)
result = ray.get(mul.remote(arr))
print(len(result))
print(result)

