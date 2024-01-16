# 3항 연산자
# [참일때의 값] if [조건문] else [거짓일때의 값]

'''
def getWeight():
    weight = float(input('몸무게 : '))
    return weight if weight >= 0 else weight * -1


w = getWeight()
print(w) 
'''

def holJJak():
    num = int(input('숫자 : '))
    return '짝수' if (num%2) == 0 else '홀수'

num = holJJak()
print(f"입력 결과 : {num}")

# 3항 연산자 중첩 가능
# [참1] if [조건1] else [참2] if [조건2] else .....

l = [13,14,15,16,17]

for i in l:
    print(f"{i}는 2의 배수") if (i%2 == 0) else print(f"{i}는 3의 배수") if (i%3 == 0) else print(f"{i}는 2의 배수도 3의 배수도 아님") 