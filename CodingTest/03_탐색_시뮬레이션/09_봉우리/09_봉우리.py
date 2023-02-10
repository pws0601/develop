import os
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
print(path)
import sys
sys.stdin=open(path+"/input.txt", "rt")

dx=[-1,0,1,0]
dy=[0,1,0,-1]

n = int(input())
a=[list(map(int, input().split())) for _ in range(n)]

# 둘레를 0으로 패딩
a.insert(0,[0]*n)
a.append([0]*n)
for x in a:
    x.insert(0, 0)
    x.append(0)

cnt=0
for i in range(1,n+1):
    for j in range(1, n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1

print(cnt)
