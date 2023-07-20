# many_user = list(map(lambda x: {'name': x[0], 'age': x[1]}, zip(name, age)))


import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users'

# API 요청
response = requests.get(API_URL)

# JSON -> list 데이터 변환
parsed_data = response.json()

# 특정 데이터(이름) 출력
dummy_data_name = []
dummy_data_lat = []
dummy_data_lng = []
dummy_data_company = []

for i in range(10):
    name = parsed_data[i]['name']
    lat = float(parsed_data[i]['address']['geo']['lat'])
    lng = float(parsed_data[i]['address']['geo']['lng'])
    company = parsed_data[i]['company']['name']
    dummy_data_name.append(name)
    dummy_data_lat.append(lat)
    dummy_data_lng.append(lng)
    dummy_data_company.append(company)


user_info = []
def data(**kwargs):
    user_info.append(kwargs)


for i, j, k, l in zip(dummy_data_name, dummy_data_lat, dummy_data_lng, dummy_data_company):
    if -80 < j < 80 and -80 < k < 80:
        data(name=i, lat=j, lng=k, company = l)

print(user_info)