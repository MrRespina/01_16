# https://dapi.kakao.com/v3/search/book
# Authorization: KakaoAK ${eb43c48551b94f0ddc100b8a8020d311}
# 책 제목 - 작가 / 할인가 / 내용 출력

from http.client import HTTPSConnection
from urllib.parse import quote
from json import loads

book = quote(input("책 이름 입력 : "))
booknum = quote(input("가져올 갯수 : "))

types = 'GET'
url = 'dapi.kakao.com'
query = '/v3/search/book?query='+book+"&size="+booknum
headers = {'Authorization': 'KakaoAK eb43c48551b94f0ddc100b8a8020d311'}

hc = HTTPSConnection(url)
hc.request(types,query,headers=headers)

res = hc.getresponse()
resBody = res.read().decode('utf-8')

bookDate = loads(resBody)

for i in range(0,len(bookDate['documents'])):
    print('*'*20)
    print(f"제목 : {bookDate['documents'][i]['title']}")   
    print(f"저자 : {bookDate['documents'][i]['authors']}")   
    print(f"내용 : {bookDate['documents'][i]['contents']}")
    if (bookDate['documents'][i]['sale_price']==-1) | (bookDate['documents'][i]['sale_price']==0):
        bookDate['documents'][i]['sale_price']='판매 중지'
    print(f"할인가 : {bookDate['documents'][i]['sale_price']}")
    

# 밑은 조금 더 편하게, 리스트만 뜯어서 가져와서 사용하는 방법.
bookss = bookDate['documents']

for i in bookss:
    print('*'*20)
    print(i['title'],'-',i['authors'][0])
    print(i['sale_price'])
    print(i['contents'])