import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users'

# API 요청
response = requests.get(API_URL)

# JSON -> list 데이터 변환
parsed_data = response.json()

# 특정 데이터(이름) 출력
dummy_data = []
for i in range(10):
    name = parsed_data[i]['name']
    dummy_data.append(name)

print(dummy_data)