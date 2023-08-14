number_of_people = 0
number_of_book = 100

def increase_user():
    global number_of_people
    number_of_people += 1
    return number_of_people

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, address):
    print(f'{name}님 환영합니다!')
    info_list = {}
    info_list['name'] = name
    info_list['age'] = age
    info_list['address'] = address
    return info_list

many_user = [] # 리스트 넣을 곳 만들고

for i in range(len(name)):      # 리스트를 할당한다
    result = create_user(name[i], age[i], address[i])
    many_user.append(result)

def decrease_book(number):
    global number_of_book
    number_of_book -= number
    print('남은 책의 수 : ',number_of_book)
    return number_of_book

def rental_book(info):       # rental_Book 함수에 인자는 info하나!  # info_list = [{}, {}]  # rental_book(info_list[0])
    name = info['name']     # info인자는 신규고객의 이름과 나이를 담은 딕셔너리
    age = info['age']
    number_of_books = age // 10         # 신규 고객의 나이를 10으로 나눈 몫을 대여할 책의 수로 활용(decreas_book 함수의 인자)
    decrease_book(number_of_books)
    print(f'{name}님이 {number_of_books}권의 책을 대여하였습니다.')

info_list = list(map(lambda user : {'name': user['name'], 'age': user['age']}, many_user))

list(map(rental_book, info_list))