import os
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
import sys
from collections import deque
sys.stdin=open(path+"/input.txt", "rt")

n=int(input())
dy=[0]*(n+1)
dy[1]=1
dy[2]=2
for i in range(3,n+1):
    dy[i]=dy[i-1]+dy[i-2]

print(dy[n])