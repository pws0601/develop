import os
from collections import deque
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
print(path)
import sys
sys.stdin=open(path+"/input.txt", "rt")

a = input()
b = input()
str1 = dict()
str2 = dict()
for x in a:
    str1[x]=str1.get(x, 0)+1
for x in b:
    str2[x]=str2.get(x, 0)+1

for i in str1.keys():
    if i in str2.keys():
        if str1[i] != str2[i]:
            print("NO")
            break
    else :
        print("NO")
else:
    print("YES")

## 개선된 코드
sH=dict()
for x in a:
    sH[x]=sH.get(x, 0)+1

for x in b:
    sH[x]=sH.get(x, 0)-1

for x in a:
    if sH.get(x) > 0:
        print("NO")
        break
else:
    print("YES")