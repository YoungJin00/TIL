# 스택

import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    words = sys.stdin.readline().split()

    if words[0] == 'push':
        stack.append(int(words[1]))

    elif words[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif words[0] == 'size':
        print(len(stack))

    elif words[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)

    elif words[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)