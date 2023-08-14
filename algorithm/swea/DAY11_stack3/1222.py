# 계산기 1
for tc in range(1, 11):
    N = int(input())
    sik = input()
    stack = []
    for i in sik:
        if i != '+':
            stack.append(int(i))

    SUM = 0
    for i in stack:
        SUM += i

    print(f'#{tc} {SUM}')
