import os
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
print(path)
import sys
sys.stdin=open(path+"/input.txt", "rt")
k, n=map(int, input().split())
Line = []


def Count(len):
    cnt=0
    for x in Line:
        cnt+=(x//len)
    return cnt

res=0
largest=0
for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    largest = max(largest, tmp)

lt=1
rt=largest
while lt<=rt:
    mid = (lt+rt)//2
    if Count(mid) >= n:
        res=mid
        lt=mid+1
    else:
        rt=mid-1

print(res)
