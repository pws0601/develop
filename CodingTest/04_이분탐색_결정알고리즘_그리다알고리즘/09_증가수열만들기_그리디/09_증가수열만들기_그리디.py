import os
from collections import deque
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
print(path)
import sys
sys.stdin=open(path+"/input.txt", "rt")

n = int(input())
a=list(map(int, input().split()))
lt=0
rt=n-1
last=0
res = ""
temp = []

while lt<=rt:
    if a[lt]>last:
        temp.append((a[lt],'L'))
    if a[rt]>last:        
        temp.append((a[rt], 'R'))        
    temp.sort()
    if len(temp)==0:
        break
    else:
        res = res+temp[0][1]
        last = temp[0][0]
        if temp[0][1] == 'L':
            lt+=1
        else :
            rt-=1
    temp.clear()
print(len(res))
print(res)