# 파리퇴치3
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
# 우 하 좌 상
dd = [ -1, -1, 1, 1]
jj = [-1, 1, 1, -1]
# 좌상 우상 우하 좌하

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    MAX = 0
    MAX1 = 0
    for i in range(N):
        for j in range(N):
            s = MAP[i][j]
            for k in range(4):
                for l in range(1, M):
                    ni, nj = i + (di[k] * l), j + (dj[k] * l)
                    if 0 <= ni < N and 0 <= nj < N:
                        s += MAP[ni][nj]
                if MAX < s:
                    MAX = s
    for i in range(N):
        for j in range(N):
            s = MAP[i][j]
            for k in range(4):
                for l in range(1, M):
                    ni, nj = i + (dd[k] * l), j + (jj[k] * l)
                    if 0 <= ni < N and 0 <= nj < N:
                        s += MAP[ni][nj]
                if MAX1 < s:
                    MAX1 = s
    total = max(MAX1, MAX)

    print(f'#{tc} {total}')