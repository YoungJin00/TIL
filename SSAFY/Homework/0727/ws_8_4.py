class Animal:
    pass

class Dog(Animal):
    def bark(self):
        print('멍 멍!')


class Cat(Animal):
    def meow(self):
        print('야 옹!')


class Pet(Dog, Cat):
    def __init__(self, a):
        super().__init__()
        self.a = a
        
    def make_sound(self):
        print(f'{self.a}')
    
    def play(self):
        print('애완동물과 놀기')



pet1 = Pet("그르르")
pet1.make_sound()
pet1.bark()
pet1.meow()
pet1.play()
