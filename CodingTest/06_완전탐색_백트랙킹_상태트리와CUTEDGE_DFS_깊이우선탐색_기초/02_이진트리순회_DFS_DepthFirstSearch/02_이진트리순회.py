import os
from collections import deque
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
print(path)
import sys
sys.stdin=open(path+"/input.txt", "rt")

def DFS(v):
    if v>7:
        return
    else:
        #print(v, end=' ') # 전위순회방식
        DFS(v*2)
        print(v, end=' ') # 중위순회방식
        DFS(v*2+1)
        #print(v, end=' ') # 후위순회방식

if __name__ == "__main__":
    DFS(1)
    print()
