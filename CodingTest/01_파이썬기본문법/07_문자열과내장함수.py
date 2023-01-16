'''
문자열과 내장함수
'''

msg = "It is Time"
print(msg.upper())
print(msg.lower())
print(msg)
tmp = msg.upper()
print(tmp)
print(tmp.find('T'))
print(tmp.count('T'))
print(msg[:2])
print(msg[3:5])
print(len(msg))
for i in range(len(msg)):
    print(msg[i], end=' ')
print()

for x in msg:
    print(x, end=' ')
print()

for x in msg:
    #if x.isupper():
    if x.islower():
        print(x, end=' ')
print()

for x in msg:
    if x.isalpha():
        print(x, end='')
print()

tmp='AZ'
for x in tmp:
    print(ord(x)) # ord함수는 입력값의 아스키 넘버 반환

tmp='az'
for x in tmp:
    print(ord(x))
    
tmp=65
print(chr(tmp)) # chr함수는 입력된 아스키 넘버값과 대응되는 문자 반환