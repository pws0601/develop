import os
from collections import deque
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
print(path)
import sys
sys.stdin=open(path+"/input.txt", "rt")

num, m = map(int, input().split())
num=list(map(int, str(num)))
stack = []
for x in num:
    while stack and m>0 and stack[-1] < x :
        stack.pop()
        m-=1
    stack.append(x)
if m!=0:
    stack=stack[:-m]

for x in stack:
    print(x, end='')
print()

res = ''.join(map(str,stack))
print(res)