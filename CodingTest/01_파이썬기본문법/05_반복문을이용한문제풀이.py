'''
반복문을 이용한 문제풀이
1) 1부터 N까지 홀수 출력하기
2) 1부터 N까지의 합 구하기
3) N의 약수출력하기


# 1 & 2 답
n = input()
n = int(n)
sum = 0
for i in range(1,n+1):
    sum +=i
    if i%2==1:
        print(i)
    
print("sum : ",sum)
'''
# 3)
n = int(input())
for i in range(1, n+1):
    if n%i==0: # n을 i로 나눠서 나머지가 0일 경우 약수
        print(i, end=' ')