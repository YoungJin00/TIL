# 10101 삼각형 외우기

sam_li = []

for i in range(3):
  n = int(input())
  sam_li.append(n)

if sum(sam_li) == 180:
  if sam_li[0]== 60 and sam_li[1]==60:
    print("Equilateral")
  elif sam_li[0] == sam_li[1] or sam_li[2] == sam_li[1] or sam_li[0] == sam_li[2]:
    print("Isosceles")
  else:
    print("Scalene")
else:
  print("Error")