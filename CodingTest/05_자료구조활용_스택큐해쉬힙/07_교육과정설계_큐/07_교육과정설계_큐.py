import os
from collections import deque
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
print(path)
import sys
sys.stdin=open(path+"/input.txt", "rt")

need = input()
n=int(input())
for i in range(n):
    plan=input()
    dq=deque(need)
    for x in plan:
        if x in dq:
            if dq.popleft() != x:
                print('#%d NO' %(i+1))
                break
    else:
        if len(dq)==0:
            print('#%d YES' %(i+1))
        else:
            print('#%d NO' %(i+1))