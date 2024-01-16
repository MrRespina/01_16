# 42008a8c8e7402a3fc9d3b1a7df8fee9
# https://api.openweathermap.org
# /data/2.5/weather?q= &appid=42008a8c8e7402a3fc9d3b1a7df8fee9&units=metrics&lang=kr

from http.client import HTTPSConnection
from urllib.parse import quote
from json import loads

city = quote(input('도시 이름 : '))
url = 'api.openweathermap.org'
query = '/data/2.5/weather?q='+city+'&appid=42008a8c8e7402a3fc9d3b1a7df8fee9&units=metric&lang=kr'

hc = HTTPSConnection(url)
hc.request('GET',query)

res = hc.getresponse() # 응답
resBody = res.read().decode('utf-8')

# print(resBody)

weatherDate = loads(resBody) # JS > Python (Dict)

# python : list > JS : array
# python : dict > JS : object

# 날씨 / 기온 / 체감기온 / 습도 / 바람속도 데이터를 콘솔창에 출력할 것.
print(f'{city}의 정보')
print(f'날씨 : {weatherDate["weather"][0]["description"]}')
print(f'기온 : {weatherDate["main"]["temp"]}\'C')
print(f'체감기온 : {weatherDate["main"]["feels_like"]}\'C')
print(f"습도 : {weatherDate['main']['humidity']}")
print(f"풍속 : {weatherDate['wind']['speed']}")