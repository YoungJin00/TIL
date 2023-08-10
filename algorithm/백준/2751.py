# 수정렬하기 2
import sys

N = int(sys.stdin.readline())
num_li = []
for i in range(N):
    num = int(sys.stdin.readline())
    num_li.append(num)

num_li.sort()

for i in num_li:
    print(i)

