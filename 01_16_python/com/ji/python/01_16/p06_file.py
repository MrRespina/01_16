# 파일 관리?
# 파일로부터 데이터를 읽어와서 프로그램에서 활용하기 위함
# 프로그램에서 만든 데이터를 파일형태로 저장하기 위함

# 파일 열기 > 작업(읽,쓰기) > 파일 닫기

# .txt / .csv

# 1. 파일에 내용 쓰기 (write)
# 폴더는 미리 만들어 놔야 함. / 파일은 존재하지 않아도 실행시 만들어 줌.

'''
file = open("C:\\Users\\sdedu\\Desktop\\Dev\\prac\\test.txt",'w',encoding='UTF-8')
file.write('하이!')
file.close()
'''

# 2. 파일에 내용 추가 (append)'\
'''
file = open("C:\\Users\\sdedu\\Desktop\\Dev\\prac\\test.txt",'a',encoding='UTF-8')
file.write('하이!\n')
file.close()
'''

# 3. 파일 읽어오기 (read)
file = open("C:\\Users\\sdedu\\Desktop\\Dev\\prac\\test.txt",'r',encoding='UTF-8')


# 3-1. 파일 전체 읽기
'''
val = file.read()
print(val)
file.close()
'''
# 3-2. 파일을 한 줄씩 읽기
while True: # 가져온 파일이 언제 끝날 지 모르기 떄문
    val2 = file.readline()
    print(val2,end="")
    if val2 == "":
        break
    
file.close()