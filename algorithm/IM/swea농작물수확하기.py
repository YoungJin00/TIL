T = int(input())

for tc in range(1, T+1):
    N = int(input())
    if not N % 2:
        break

    MAP = [list(map(int, input())) for _ in range(N)]
    dot = N // 2
    res = 0
    for i in range(N):
        if i <= dot:
            for j in range(dot - i, dot+1+i):
                res += MAP[i][j]
        else:
            for j in range(i - dot, N-i+dot):
                res += MAP[i][j]

    print(f'#{tc} {res}')