'''
대표값 문제 오류 수정
round는 round_half_even 방식을 택한다.
round_half_up 5 이상은 올림
round_half_even 정확하게 half지점일 경우 짝수쪽으로 간다.
'''
## round_half_even이기때문에 4가 나온다.
## 4.500 경우 짝수인 4
## 5.500 경우 짝수인 6
a = 4.5000
print(round(a))

a=66.6
a=a+0.5
a=int(a)
print(a)
