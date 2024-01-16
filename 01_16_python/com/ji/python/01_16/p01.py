'''
Created on 2024. 1. 16.

@author: sdedu
'''
from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring
from urllib.parse import quote

# 6pWWvJLlnH7wUuihsKay
# JOdlXI05N4

# https://openapi.naver.com/v1/search/shop.xml

def rmb(t):
    t = t.replace('<b>','').replace('</b>','')
    return t

# 상품명 : 입력
# 결과 > xml 파싱
# title,lprice,brand,category1에 대한 정보 출력할 것.

item = input('상품 명  : ')
q = quote(item)
num = quote(input('요청 갯수 : '))

# URLEncoding해서 주소로 넘길 것
myid = '6pWWvJLlnH7wUuihsKay'
secret = 'JOdlXI05N4' 

hds = { 
    'X-Naver-Client-Id': myid, 
    'X-Naver-Client-Secret': secret
}

url = '/v1/search/shop.xml?query='+q+'&display='+num

hc = HTTPSConnection('openapi.naver.com')
hc.request('GET',url,headers=hds)

res = hc.getresponse() # 응답
resBody = res.read().decode('utf-8')

for i in fromstring(resBody).getiterator('item'):
    print(rmb(i.find('title').text))
    print(i.find('lprice').text)
    print(i.find('brand').text)
    print(i.find('category1').text)
    print('*'*20)
    
    
    
