import ray

ray.init("ray://localhost:10001")

@ray.remote
def do_work(x):
    return x ** x

do_work.remote(2)