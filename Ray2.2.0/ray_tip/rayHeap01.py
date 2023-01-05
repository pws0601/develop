import ray
import numpy as np
import sys

ray.init()

# 메모리 증가 문제가 발생
@ray.remote
def large_values(num_returns):
    return [
        np.random.randint(np.iinfo(np.int8).max, size=(100_000_000,1), dtype=np.int8)
        for _ in range(num_returns)
    ]


# yield로 반환값을 제너레이터로 생성하여 메모리 문제 해결
@ray.remote
def large_values_generator(num_returns):
    for i in range(num_returns):
        yield np.random.randint(
            np.iinfo(np.int8).max, size=(100_000_000, 1), dtype=np.int8
        )
        print(f"yielded return value {i}")

# A large enough value (e.g. 100)
num_returns = 100

"""
print("Using normal functions...")
try:
    ray.get(
        large_values.options(num_returns=num_returns, max_retries=0). remote(
            num_returns
        )[0]
    )
except ray.exceptions.WorkerCrashedError:
    print("Worker failed with normal function")
"""

print("Using generators...")
ray.get(
    large_values_generator.options(num_returns=num_returns, max_retries=0). remote(
            num_returns
        )[0]
)
print("Success!")
