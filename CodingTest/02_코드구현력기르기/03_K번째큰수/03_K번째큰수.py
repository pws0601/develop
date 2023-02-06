import os
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
print(path)
import sys
sys.stdin=open(path+"/input.txt", "rt")

n, k=map(int, input().split())
a=list(map(int, input().split()))

#중복을 제거하는 자료구조 set()
res = set()
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])

#res를 list 형변환
res = list(res)
res.sort(reverse=True)
print(res[k-1])

