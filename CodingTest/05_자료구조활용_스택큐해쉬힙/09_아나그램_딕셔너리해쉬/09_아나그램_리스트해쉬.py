import os
from collections import deque
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
print(path)
import sys
sys.stdin=open(path+"/input.txt", "rt")

a=input()
b=input()
str1=[0]*52
str2=[0]*52

#ord() 입력값의 아스키코드 반환 함수
for x in a:
    if x.isupper():
        str1[ord(x)-65]+=1
    else:
        str1[ord(x)-71]+=1

for x in b:
    if x.isupper():
        str2[ord(x)-65]+=1
    else:
        str2[ord(x)-71]+=1

# python스럽게 비교
if str1==str2:
    print("YES")
else :
    print("NO")

# 오리지널 비교
for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")