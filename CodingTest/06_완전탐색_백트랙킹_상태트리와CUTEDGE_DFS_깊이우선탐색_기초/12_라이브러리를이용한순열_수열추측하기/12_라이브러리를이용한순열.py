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
n, f=map(int, input().split())
b=[1]*n
for i in range(1, n):
    b[i]=b[i-1]*(n-i)/i
a=list(range(1,n+1))
cnt=0
for tmp in it.permutations(a):
    sum=0
    for L, x in enumerate(tmp):
        sum += (x*b[L])
    if sum==f:
        for x in tmp:
            print(x, end=' ')
        break    
