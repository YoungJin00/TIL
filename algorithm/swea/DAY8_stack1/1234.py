# 비밀번호

for tc in range(1, 11):
    N, num = input().split()
    N = int(N)
    stack = []
    li = []
    for i in num:
        if stack:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    print(f'#{tc} ', end='')
    for i in stack:
        print(i, end='')
    print()