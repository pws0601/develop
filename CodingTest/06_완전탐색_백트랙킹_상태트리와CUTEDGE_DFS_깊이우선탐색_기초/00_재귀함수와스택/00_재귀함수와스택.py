import os
from collections import deque
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
print(path)
import sys
sys.stdin=open(path+"/input.txt", "rt")

def DFS(x):
    if x > 0:        
        DFS(x-1)
        print(x, end=' ')

if __name__ == "__main__":
    n=int(input())
    DFS(n)