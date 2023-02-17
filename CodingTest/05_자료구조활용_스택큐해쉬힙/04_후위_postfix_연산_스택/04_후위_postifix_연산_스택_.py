import os
from collections import deque
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
print(path)
import sys
sys.stdin=open(path+"/input.txt", "rt")

a=input()
stack=[]
for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        n1 = stack.pop()
        n2 = stack.pop()
        if x =='+':
            stack.append(n2+n1)
        elif x=='-':
            stack.append(n2-n1)
        elif x=='*':
            stack.append(n2*n1)
        elif x=='/':
            stack.append(n2/n1)
print(stack)
        