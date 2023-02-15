import os
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
print(path)
import sys
sys.stdin=open(path+"/input.txt", "rt")

n = int(input())
metting=[]
for i in range(n):
    s, e = map(int, input().split())
    metting.append((s,e))
# 튜플의 앞의 성분으로 정렬
#metting.sort()
# 튜플의 정렬 순위를 앞, 뒤 변경
metting.sort(key=lambda x : (x[1], x[0]))
et=0
cnt=0
for s, e in metting:
    if s>=et:
        et=e
        cnt+=1

print(cnt)
