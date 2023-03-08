import os
from collections import deque
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
import sys
sys.stdin=open(path+"/input.txt", "rt")
input=sys.stdin.readline

def DFS(L):
    global res
    if L==n:
        char=max(money)-min(money)
        if char<res:
            tmp=set()
            for x in money:
                tmp.add(x)
            if len(tmp)==3:
                res = char
    else:
        for i in range(3):
            money[i] += coin[L]
            DFS(L+1)
            money[i] -= coin[L]


if __name__=="__main__":
    n=int(input())
    coin=[]
    money=[0]*3
    res=2147000000
    for _ in range(n):
        coin.append(int(input()))
    DFS(0)
    print(res)