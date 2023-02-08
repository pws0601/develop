import os
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
print(path)
import sys
sys.stdin=open(path+"/input.txt", "rt")

# 숫자만 추출
s = input()
res = 0
for x in s:
    if x.isdecimal() :
        res=res*10+int(x)

print(res)

# 추출된 숫자의 약수 구하기
# 약수는 1부터 숫자만큼 1씩 커지면서 나눈 나머지가 0일경우 약수
cnt=0
for i in range(1, res+1):
    if res%i==0:
        cnt+=1
print(cnt)