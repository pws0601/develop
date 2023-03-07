import os
from collections import deque
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
print(path)
import sys
# 수열을 만들어주는 모듈
import itertools as it
sys.stdin=open(path+"/input.txt", "rt")
input=sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())

cnt = 0
for x in it.combinations(a, k):
    if sum(x)%m == 0 :
        cnt += 1

print(cnt)