import os
from collections import deque
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
print(path)
import sys
sys.stdin=open(path+"/input.txt", "rt")

n, limit = map(int, input().split())
p=list(map(int, input().split()))
p.sort()
p=deque(p)
cnt = 0
while p:
    if len(p)==1:
        cnt += 1
        break
    if p[0] + p[-1] > limit:
        p.pop()
        cnt += 1
    else:
        #p.pop(0) # list 자료구조에서 사용
        p.popleft() # deque 자료구조에서 사용
        #deque 자료구조는 list 와는 다르게 양 옆을 pop하는데 효과적인 자료구조이다.

        p.pop()
        cnt +=1
print(cnt)
    