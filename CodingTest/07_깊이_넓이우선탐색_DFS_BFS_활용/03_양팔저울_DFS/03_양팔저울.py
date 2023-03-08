import os
from collections import deque
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
import sys
sys.stdin=open(path+"/input.txt", "rt")
input=sys.stdin.readline

def DFS(L, sum):
    global res
    if L==n:
        if 0<sum<=s:
            res.add(sum)
    else:
        DFS(L+1, sum+G[L])
        DFS(L+1, sum-G[L])
        DFS(L+1, sum)


if __name__ == "__main__":
    n = int(input())
    G=list(map(int, input().split()))
    s = sum(G)
    res = set()
    DFS(0, 0)
    print(s-len(res))