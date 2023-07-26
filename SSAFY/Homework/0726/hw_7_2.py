# hw_7_2.py

# 아래 클래스를 수정하시오.
class StringRepeater:    
    def repeat_string(self, i, c):
        for _ in range(i):
            print(c)
    

repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")
