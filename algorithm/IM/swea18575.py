di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    total_max = 0
    total_min = float('INF')
    for i in range(N):
        for j in range(N):
            s = MAP[i][j]
            for k in range(4):
                for l in range(1, N):
                    ni, nj = i + di[k] * l, j + dj[k] * l
                    if 0 <= ni < N and 0 <= nj < N:
                        s += MAP[ni][nj]
            if total_max < s:
                total_max = s

            if total_min > s:
                total_min = s

    res = total_max - total_min
    print(f'#{tc} {res}')




