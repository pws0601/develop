import os
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
print(path)
import sys
sys.stdin=open(path+"/input.txt", "rt")

n, m = map(int, input().split())
a=list(map(int, input().split()))


## 이분 탐색
# 전체 범위를 반씩 나눠서 탐색하는 방법

a.sort()
lt=0
rt=n-1
while lt<=rt:
    mid = (lt+rt)//2
    if a[mid] == m : 
        print(mid+1)
        break
    elif a[mid] > m:
        rt=mid-1
    else :
        lt=mid+1
