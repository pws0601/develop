"""
변수명 정하기
1) 영문과 숫자, _ 로 이루어진다.
2) 대소문자를 구분한다.
3) 문자나, _로 시작한다.
4) 특수문자를 사용하면안된다. ($, % 등)
5) 키워드를 사용하면 안된다. (if, for 등)
"""

a=1
A=2
A1=3
#2b=4 변수명은 문자나, _로 시작해야함.
_2b=4
print(a, A, A1, _2b)
# 변수를 한꺼번에 선언하고 값을 초기화 할수 있다.
a, b, c = 3, 2, 1
print(a, b, c)

# 값 교환
a, b=10, 20
print(a, b)
a, b= b, a
print(a, b)

# 변수 타입
# int
a=12345
print(type(a))
print(a)

#float
# 실수형은 8바이트 사이즈를 갖는다.8바이트를 넘기면 데이터가 손실된다.
a=12.123456789123456789
print(type(a))
print(a)

#str
a='student'
print(type(a))
print(a)

# 출력방식
print("number")
a, b, c = 1, 2, 3
print(a, b, c)
print("number : ", a, b, c)
# sep='' seperator 지정
print(a, b, c, sep='')
print(a, b, c, sep=', ')
print(a, b, c, sep=',')
print(a, b, c, sep='\n')
# end='' 마지막 조건 변경
print(a, end= ' ')
print(b, end= ' ')
print(c)