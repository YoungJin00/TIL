# 차르봄바

T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(1, T+1):
    N, P = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    res = 0

    for i in range(N):
        for j in range(N):
            s = MAP[i][j]
            for k in range(4):
                for l in range(1, P+1):
                    ni, nj = i + di[k] * l, j + dj[k] * l
                    if 0 <= ni < N and 0 <= nj < N:
                        s += MAP[ni][nj]
            if res < s:
               res = s
    print(f'#{tc} {res}')


