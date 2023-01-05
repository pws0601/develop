import ray

ray.init()

import numpy as np

@ray.remote
def create_matrix(size):
    return np.random.normal(size=size)

@ray.remote
def multiply_matrices(x,y):
    return np.dot(x,y)


x_id = create_matrix.remote([1000, 1000])
y_id = create_matrix.remote([1000, 1000])
z_id = multiply_matrices.remote(x_id,y_id)

z = ray.get(z_id)

print(z)

ray.shutdown()
