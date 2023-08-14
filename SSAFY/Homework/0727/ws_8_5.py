# ws_8_5.py

class Animal:
    pass

class Dog(Animal):
    sound = '멍멍'
    def bark(self):
        print('멍 멍!')


class Cat(Animal):
    sound = '야옹'
    def meow(self):
        print('야 옹!')


class Pet(Cat, Dog):
    def __init__(self, a):
        super().__init__()
        self.a = a
        
    def make_sound(self):
        print(f'{self.a}')
    
    def play(self):
        print('애완동물과 놀기')
    
    def __str__(self):
       return f'애완동물은 {self.sound} 소리를 냅니다.'



pet1 = Pet("그르르")
print(pet1)

