# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     answer = 0
#
#     dx = [0, 1, 0, -1]
#     dy = [1, 0, -1, 0]
#
#     for y in range(N):
#         for x in range(N):
#             for idx in range(4):
#                 nx = x + dx[idx]
#                 ny = y + dy[idx]
#
#                 if 0 <= nx < N and 0 <= ny < N:
#                     answer += abs(arr[ny][nx] - arr[y][x])
#
#     print(f'#{tc} {answer}')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = 0

    for i in range(N):
        for j in range(N):
            s = arr[i][j]
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ni, nj = i + di, j + dj

                if 0 <= ni < N and 0 <= nj < N:
                    res += abs(arr[ni][nj] - s)

    print(f'#{tc} {res}')