import os
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
print(path)
import sys
sys.stdin=open(path+"/input.txt", "rt")

n=int(input())
a=list(map(int, input().split()))

sum=0
cnt=0

for x in a:
    if x==1:
        cnt+=1
        sum+=cnt
    else:
        cnt=0

print(sum)