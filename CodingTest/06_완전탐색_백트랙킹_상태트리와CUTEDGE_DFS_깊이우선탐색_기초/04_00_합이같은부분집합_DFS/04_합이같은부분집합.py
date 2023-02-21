import os
from collections import deque
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
print(path)
import sys
sys.stdin=open(path+"/input.txt", "rt")

def DFS(L, sum):
    if sum>total//2:
        return
    if L == n:        
        if sum==(total-sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)


if __name__=="__main__":
    n = int(input())
    a=list(map(int, input().split()))
    total = sum(a)
    DFS(0,0)
           