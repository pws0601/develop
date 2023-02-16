import os
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
print(path)
import sys
sys.stdin=open(path+"/input.txt", "rt")

L = int(input())
a = list(map(int, input().split()))
m = int(input())

a.sort()
for _ in range(m):
    a[0] += 1
    a[L-1] -= 1
    a.sort()
print(a[L-1] - a[0])