import os
path = os.path.realpath(__file__)
path = path[0:path.rfind("/")]
print(path)
import sys
sys.stdin=open(path+"/input.txt", "rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
for x in a:
    print(x)

largest=-2147000000

for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1+=a[i][j]
        sum2+=a[j][i]
    if sum1>largest:
        largest = sum1
    elif sum2>largest:
        largest = sum2

sum1=sum2=0
for i in range(n):
    sum1+=a[i][i]
    sum2+=a[i][n-i-1]    
if sum1>largest:
    largest = sum1
elif sum2>largest:
    largest = sum2

print(largest)
