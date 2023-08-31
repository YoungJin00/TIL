# 스택 수열

import sys
input = sys.stdin.readline

N = int(input())

lst = [int(input()) for _ in range(N)]
stack = []
res = []

num = 1
for i in lst:
    while num <= i:
        stack.append(num)
        res.append('+')
        num += 1

    if stack[-1] == i:
        stack.pop()
        res.append('-')
    else:
        print("NO")
        exit()

for j in res:
    print(j)