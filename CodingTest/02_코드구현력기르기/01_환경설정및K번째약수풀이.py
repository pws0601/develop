'''
약수는 1부터 자기자신까지의 숫자로 나눴을때 나머지가 0인 수
탐색할 숫자 n, 알고싶은 번째 k

문제 입력 숫자 n의 k번째 약수를 구하여라 
'''
n, k=map(int, input().split())
cnt=0
for i in range(1, n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else:
    print(-1)