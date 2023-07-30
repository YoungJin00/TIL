# 대지 9063
n = int(input())
x_li = []
y_li = []

for i in range(n):
   a = list(map(int, input().split()))
   if n == 1:
      break
   x_li.append(a[0])
   y_li.append(a[1])

print((max(x_li) - min(x_li)) * (max(y_li) - min(y_li)) )






