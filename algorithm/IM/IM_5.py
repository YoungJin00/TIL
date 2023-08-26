# 중계기

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N+1)]

    for i in range(N+1):
        for j in range(N+1):
            if MAP[i][j] == 2:
                y = i
                x = j

    MAX = 0
    d = 0
    for k in range(N+1): # 행
        for l in range(N+1): # 열
            if MAP[k][l] == 1:
                d = (x - l)**2 + (y - k)**2
                if MAX < d:
                    MAX = d

    MAX = MAX**(1/2)

    if MAX == int(MAX):
        MAX = int(MAX)
    else:
        MAX = int(MAX) + 1

    print(f'#{tc} {MAX}')
