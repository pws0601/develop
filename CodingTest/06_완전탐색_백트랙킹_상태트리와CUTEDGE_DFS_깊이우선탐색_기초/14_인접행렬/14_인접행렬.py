import os
from collections import deque
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
import sys
sys.stdin=open(path+"/input.txt", "rt")
input=sys.stdin.readline

n, m = map(int, input().split())
g = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = c    

for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end=' ')
    print()

