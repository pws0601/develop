import os
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
print(path)
import sys
sys.stdin=open(path+"/input.txt", "rt")

n=int(input())
a=list(map(int, input().split()))

def reverse(x):
    res = 0
    while x>0:
        t=x%10
        res=res*10+t
        x=x//10
    return res

def isPrime(x):
    if x==1:
        return False
    for i in range(2, x//2+1): # 약수는 2를 곱하는 값이기때문에 x의 반까지만 돌면 된다.
        if x%i==0:
            return False
    else:
        return True

for x in a:
    tmp=reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')

