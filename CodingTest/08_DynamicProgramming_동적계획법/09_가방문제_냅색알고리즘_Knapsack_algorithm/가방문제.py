import os
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
import sys
from collections import deque
sys.stdin=open(path+"/input.txt", "rt")

if __name__=="__main__":
    n, m=map(int, input().split())
    dy=[0]*(m+1)
    for i in range(n):
        w, v = map(int, input().split())
        for j in range(w, m+1):
            dy[j]=max(dy[j],dy[j-w]+v)
    print(dy[m])