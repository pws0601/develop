import ray
import datetime
import time

print(ray.__version__)

ray.init()

# ray task 정의
# @ray.remote 데코레이션 추가
@ray.remote
def print_current_datetime():
    time.sleep(0.3)
    current_datetime = datetime.datetime.now()
    return current_datetime

#current_datetime = ray.get(print_current_datetime.remote())
#print("current_datetime : ",current_datetime)

futures = [print_current_datetime.remote() for i in range(4)]
print(futures)

print(ray.get(futures))

#ray.shutdown()
