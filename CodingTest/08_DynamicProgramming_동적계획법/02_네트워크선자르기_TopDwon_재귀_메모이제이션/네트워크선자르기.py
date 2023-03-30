import os
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
import sys
from collections import deque
sys.stdin=open(path+"/input.txt", "rt")


def DFS(len):
    if dy[len]>0:
        return dy[len]
    if len==1 or len==2:
        return len
    else:
        dy[len]=DFS(len-1)+DFS(len-2)
        return dy[len]

if __name__=="__main__":
    n=int(input())
    dy=[0]*(n+1)
    print(DFS(n))