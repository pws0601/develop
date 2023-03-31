import os
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
import sys
from collections import deque
sys.stdin=open(path+"/input.txt", "rt")

if __name__ == "__main__":
    n=int(input())
    coin=list(map(int,input().split()))
    m=int(input())
    dy=[1000]*(m+1)
    dy[0]=0
    for i in range(n):
        for j in range(coin[i], m+1):
            dy[j]=min(dy[j],dy[j-coin[i]]+1)
    print(dy[m])