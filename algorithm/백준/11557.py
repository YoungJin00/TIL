# 11557

t = int(input())
school = ''
cnt = 0

for tc in range(t):
  n = int(input())
  for i in range(n):
    a, b =input().split()
    b = int(b)
    if(b > cnt):
        cnt = b
        school = a

  print(school)



