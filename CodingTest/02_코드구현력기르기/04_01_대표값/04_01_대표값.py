import os
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
print(path)
import sys
sys.stdin=open(path+"/input.txt", "rt")

n=int(input())
a=list(map(int, input().split()))
min=2147000000
score = 0
# 평균 구하기
ave=round(sum(a)/n)
for idx, x in enumerate(a):
    # abs() 절댓값
    tmp = abs(x-ave)
    if tmp<min:
        min=tmp
        score=x
        res=idx+1
    elif tmp==min:
        if x>score:
            score = x
            res = idx+1
print(ave, res)