import requests
from pprint import pprint as print

dummy_data = []
for i in range(1, 11):
    user_info = {}
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    response = requests.get(API_URL).json()
    if (
        -80 < float(response['address']['geo']['lat']) < 80
        and -80 < float(response['address']['geo']['lng']) < 80
    ):
        user_info = {
            'name': response['name'],
            'lat': response['address']['geo']['lat'],
            'lng': response['address']['geo']['lng'],
            'company': response['company']['name'],
        }
        dummy_data.append(user_info)

black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']

def censorship(data):
    if data['company'] in black_list:
        print(f'{data["company"]} 소속의 {data["name"]} 은/는 등록할 수 없습니다.')
        return False
    else:
        print('이상 없습니다.')
        return True

def create_user(dummy_data):
    censored_user_list = {}
    for data in dummy_data:
        if censorship(data):
            if censored_user_list.get(data['company']):
                censored_user_list.get(data['company']).append(data['name'])
            else:
                censored_user_list[data['company']] = [data['name']]
    return censored_user_list

print(create_user(dummy_data))