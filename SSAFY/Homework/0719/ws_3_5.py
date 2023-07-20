number_of_book = 100

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

def increase_user():
    pass

user_info = []
def create_user(**kwargs):
    user_info.append(kwargs)


for i, j, k in zip(name, age, address):
    print(f'{i}님 환영합니다 !')
    create_user(name=i, age=j, address=k)


many_user = list(map(lambda x: {'name': x[0], 'age': x[1]}, zip(name, age)))
# print(many_user)

def rental_book(info):
    num_books = info['age'] // 10 # 신규 고객의 나이를 10으로 나눈 몫을 대여할 책의 수로 활용
    decrease_book(num_books)
    print(f"{info['name']}님이 {num_books}권의 책을 대여하였습니다.")

def decrease_book(number):
    global number_of_book
    number_of_book -= number
    print('남은 책의 수:', number_of_book)

for user_info in many_user:
    rental_book(user_info)
