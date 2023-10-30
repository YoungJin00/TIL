islogined = False

def check_login():
    if islogined:
        return True

# 전처리, 후처리 로직이 너무 길다!
# 중복되는 코드가 너무 많이 발생 !!! > 이걸 어떻게 없앨까 ?
# 파이썬의 데코레이터를 활용 !!


# myFunc : 핵심 로직을 구현한 함수


def my_decorator(func):
    def wrapper():
        # 전처리
        if not islogined:
            print('로그인하고와라')
            return
        
        func()
        # 후처리
        print('로직 끝남')
    return wrapper

@my_decorator
def myFunc():
    print('myfunc')


myFunc()
