import os
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
print(path)
import sys
sys.stdin=open(path+"/input.txt", "rt")

for _ in range(10):
    a=list(range(21))
    s, e=map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]
    a.pop(0)
    for x in a:
        print(x, end=' ')
    print()