import os
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
print(path)
import sys
sys.stdin=open(path+"/input.txt", "rt")

n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]

for x in a:
    print(x)


res = 0
s=e=n//2
for i in range(n):
    for j in range(s, e+1):        
        res+=a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else :         
        s+=1
        e-=1
print(res)