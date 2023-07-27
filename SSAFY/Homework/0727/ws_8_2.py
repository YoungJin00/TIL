# ws_8_2.py

# 아래 클래스를 수정하시오.
class Animal:
    pass

    
class Dog(Animal):
    def bark(self):
        print('멍 멍!')

class Cat(Animal):
    pass

class Pet(Dog, Cat):
    pass

dog1 = Dog()
dog1.bark()
