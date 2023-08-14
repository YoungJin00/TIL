# 숫자의 개수

A = int(input())
B = int(input())
C = int(input())
num = [0] * 10

x = A * B * C

for i in str(x):
    num[int(i)] += 1

for j in num:
    print(j)