# 풍선팡2

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    ball = [list(map(int, input().split())) for _ in range(N)]

      #  우  하  좌  상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    total = 0

    for i in range(N):
        for j in range(M):
            sum_ball = ball[i][j]
            for k  in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    sum_ball += ball[ni][nj]
            if total < sum_ball:
                total = sum_ball
    print(f'#{tc} {total}')


