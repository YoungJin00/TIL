# ws_7_2.py

# 아래 클래스를 수정하시오.
class Shape:
   def __init__(self, width, height):
      self.width = width
      self.height = height
   
   def calculate_area(self):
      return self.width * self.height

# 튜플 활용
# class Shape:
#    def __init__(self, width, height):
#       self.a = (width, height)
   
#    def calculate_area(self):
#       return self.a[0] * self.a[1]


shape1 = Shape(5, 3)
area1 = shape1.calculate_area()
print(area1)