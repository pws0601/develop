import os
from collections import deque
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
import sys
sys.stdin=open(path+"/input.txt", "rt")
input=sys.stdin.readline

def DFS(L, P):
    global cnt
    if L==n:
        cnt+=1
        for j in range(P):
            print(chr(res[j]+64), end='')
        print()
    else:
        for i in range(1, 27):
            if code[L]==i:
                res[P] = i
                DFS(L+1, P+1)
            elif i>=10 and code[L]==i//10 and code[L+1]==i%10:
                res[P]=i
                DFS(L+2, P+1)


if __name__=="__main__":
    code=list(map(int, input()))
    n=len(code)
    code.insert(n, -1)
    res=[0]*(n+3)
    cnt=0
    DFS(0, 0)
    print(cnt)