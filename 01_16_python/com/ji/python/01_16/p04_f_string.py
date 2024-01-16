'''
Created on 2024. 1. 16.

@author: sdedu
'''
from _datetime import datetime
'''
# 좋아하는 음료 이름, 마시는 횟수 > 입력 받아서 그 내용을 출력
drink = input('음료 : ')
count = int(input('마시는 횟수 : '))

print('저는 %s를 좋아하고, 하루 %d 잔을 마십니다.'%(drink,count))
print('*'*40)

print('저는 {0}를 좋아하고, 하루 {1} 잔을 마십니다.'.format(drink, count))
print('*'*40)

print(f'저는 {drink}를 좋아하고, 하루 {count} 잔을 마십니다.')
print('*'*40)

print(f'저는 {drink}를 좋아하고, 하루 {count:.2f} 잔을 마십니다.')



'''
f = 1.125
f2 = 1.135

print(f'{f}') # 1.125
print(f'{f:.1f}') # 1.1
print(f'{f:.2f}') # 1.12

print(f'{f2}') # 1.135
print(f'{f2:.1f}') # 1.1
print(f'{f2:.2f}') # 1.14

# python의 반올림은 반올림하려는 수가 올림,내림 했을 때 동일하게 차이가 나는 경우에는 (5가 기준이 되는 경우)
# 0,1,2는 반올림 처리가 안된다. (파이썬에서 실수를 나타낼 때는 2진수의 소수여서, 반올림이 안됨.)



# 문자 정렬
s1 = 'left'
result1 = f'|{s1:<10}|'
print(result1)

s2 = 'mid'
result2 = f'|{s2:^10}|'
print(result2)

s3 = 'left'
result3 = f'|{s1:>10}|'
print(result3)

# 중괄호 안에 있는 변수 뒤에 : 붙이고 < , ^ , > 로 문자열 정렬 가능.
# 뒤의 자릿수는 총 문자의 갯수이다.


# f-string에서 중괄호 출력
num = 10
result4 = f"my age: {num},{{num}},{{{num}}}"
print(result4)



# f-string과 dict
d = {'name':'Pin','gender':'men','age':30}
res5 = f"name:{d['name']}\ngender:{d['gender']}\nage:{d['name']}"
print(res5)

# f-string과 list
n = [100,200,300]
res6 = f"{n[0]},{n[1]},{n[2]}"
print(res6)


cnt = 0
for v in n:
    cnt = cnt + 1
    print(f'리스트 {cnt}번 : {v}')
    

num2 = 1234567890
print(f"{num2:,}")

date = datetime.today()
print(date)

print(f"{date:%Y-%m-%d} is on a {date:%A}")






'''
정리
    1. 문자열 맨 앞에 f 붙일 것.
    2. 사용하고 싶은 변수, 값을 중괄호({})에 넣을 것
    3. 입맛대로 커스터마이징
'''




