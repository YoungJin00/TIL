name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

my_dict = {}  # 빈 딕셔너리 생성

# 리스트의 길이를 기준으로 반복하여 딕셔너리에 값들 추가
# for i in range(len(name)):
#     key = f'key{i}'  # 키 생성
#     value = {
#         'name': name[i],
#         'age': age[i],
#         'address': address[i]
#     }  # 값 생성
#     my_dict[key] = value  # 딕셔너리에 항목 추가

# # 딕셔너리 출력
# print(my_dict)

# def create_user(name, age, address):
#     global user_info
#     user_info['name'] = name
#     user_info['age'] = age
#     user_info['address'] = address
#     print(f'{name}님 환영합니다')

# user_info = {}
# li = []
# for i, j, k in zip(name, age, address):
#     user_info['name'] = i
#     user_info['age'] = j
#     user_info['address'] = k
#     print(f'{i}님 환영합니다 !')
# print(li)


# user_info = []
# def create_user(**kwargs):
#     user_info.append(kwargs)
#     # print(kwargs)



# for i, j, k in zip(name, age, address):
#     print(f'{i}님 환영합니다 !')
#     create_user(name = i, age= j, address = k )
    
# print(user_info)

user_info = []
def create_user(**kwargs):
    user_info.append(kwargs)
    # print(kwargs)



for i, j, k in zip(name, age, address):
    print(f'{i}님 환영합니다 !')
    create_user(name = i, age= j, address = k )
    pi = list(map(dict, user_info))
    
print(pi)



