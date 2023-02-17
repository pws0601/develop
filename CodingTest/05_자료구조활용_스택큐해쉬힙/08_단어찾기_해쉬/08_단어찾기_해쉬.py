import os
from collections import deque
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
print(path)
import sys
sys.stdin=open(path+"/input.txt", "rt")

n = int(input())
p = dict()
for i in range(n):
    word = input()
    p[word]=1
for i in range(n-1)    :
    word = input()
    p[word] = 0
for key, val in p.items():
    if val==1:
        print(key, val)