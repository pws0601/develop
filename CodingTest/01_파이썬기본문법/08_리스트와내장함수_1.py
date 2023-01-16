'''
리스트와 내장함수(1)
'''
import random as r
b=list()
#print(b)

a=[1, 2, 3, 4, 5]
#print(a)
#print(a[0])

b=list(range(1, 11))
#print(b)

c = a+b
#print(c)

print(a)
a.append(6)
print(a)

a.insert(3, 7)
print(a)

a.pop() # list에서 맨 뒤를 제거 한다.
print(a)

a.pop(3) # 3번 인덱스의 값을 제거
print(a)

a.remove(4) # 4 값을 찾아서 제거 
print(a)

print(a.index(5)) # 5 값의 index 를 리턴

a=list(range(1, 11))
print(a)
print(sum(a)) # a list의 합을 출력
print(max(a)) # a list의 가장 큰값을 찾는다
print(min(a)) # a list의 가장 작은값을 찾는다
print(min(7, 5)) # 인자값중 최소값을 찾는다. 5
print(min(7, 3, 5))
print(a)
r.shuffle(a) # a 리스트를 무작위로 shuffle
print(a)
a.sort(reverse=True) # 내림차순 정렬
print(a)
a.sort() # 오름차순 정렬
print(a)
a.clear() # list를 초기화
print(a)