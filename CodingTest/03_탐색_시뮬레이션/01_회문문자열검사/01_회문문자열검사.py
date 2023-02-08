import os
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
print(path)
import sys
sys.stdin=open(path+"/input.txt", "rt")

# 회문 문자열이란?
# 앞으로 읽으나 뒤로 읽으나 같은 문자열
n = int(input())

for i in range(n):
    s=input()
    # 대소문자 구분 안함
    s=s.upper()
    ## 1 case
    size = len(s)
    for j in range(size//2):
        if s[j] != s[-1 -j] : 
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))
    
    ## 2 case
    ## s[::-1] 문자열을 뒤집는 python스러운 문법
    if s == s[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))
