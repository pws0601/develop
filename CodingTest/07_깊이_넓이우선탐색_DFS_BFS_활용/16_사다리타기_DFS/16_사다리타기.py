import os
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
import sys
from collections import deque
sys.stdin=open(path+"/input.txt", "rt")

def DFS(x, y):
    ch[x][y] = 1
    if x==0:
        print(y)
    else : 
        if y-1>=0 and board[x][y-1]==1 and ch[x][y-1] == 0:
            DFS(x, y-1)
        elif y+1<10 and board[x][y+1] == 1 and ch[x][y+1] == 0:
            DFS(x, y+1)
        else:
            DFS(x-1, y)




if __name__=="__main__" : 
    board=[list(map(int, input().split())) for _ in range(10)]
    ch=[[0]*10 for _ in range(10)]
    for y in range(10):
        if board[9][y]==2:
            DFS(9,y)