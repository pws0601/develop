import os
from collections import deque
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
import sys
sys.stdin=open(path+"/input.txt", "rt")
input=sys.stdin.readline

def DFS(L, sum, time):
    global res
    if time>m:
        return
    if L==n:
        if sum>res:
            res=sum
    else:
        DFS(L+1, sum+pv[L], time+pt[L])
        DFS(L+1, sum, time)



if __name__=="__main__":
    n, m=map(int, input().split())
    pv=list()
    pt=list()
    for i in range(n):
        a, b=map(int, input().split())
        pv.append(a)
        pt.append(b)
    res=-2147000000
    DFS(0, 0, 0)
    print(res)