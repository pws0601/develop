import os
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
print(path)
import sys
sys.stdin=open(path+"/input.txt", "rt")

n=int(input())
a=list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    while x>0:
        sum+=x%10
        x=x//10
    return sum

def digit_sum2(x):
    sum = 0
    for i in str(x):
        sum+=int(i)
    return sum

max = -2147000000
for x in a:
    tot=digit_sum2(x)
    if tot > max:
        max=tot
        res = x
print(res)