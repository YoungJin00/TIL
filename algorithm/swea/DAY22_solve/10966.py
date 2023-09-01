# from collections import deque
#
#
# def dfs(n, m, MAP):
#     global visited
#     q = deque()
#
#     for i in range(n):
#         for j in range(m):
#             if MAP[i][j] == 'W':
#                 q.append((i, j))
#                 visited[i][j] = 0
#     while q:
#         x, y = q.popleft()
#         for k in range(4):
#             ni, nj = x + di[k], y + dj[k]
#             if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == -1:
#                 q.append((ni, nj))
#                 visited[ni][nj] = visited[x][y] + 1
#     res = 0
#     for i in range(n):
#         for j in range(m):
#             res += visited[i][j]
#     return res
#
#
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     MAP = [list(input()) for _ in range(N)]
#     visited = [[-1] * M for _ in range(N)]
#     ans = dfs(N, M, MAP)
#
#     print(f'#{tc} {ans}')

from collections import deque
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    MAP = [list(input()) for _ in range(N)]
    visited = [[-1]*M for _ in range(N)]

    q = deque()

    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 'W':
                q.append((i,j))
                visited[i][j] = 0

    while q:
        x, y = q.popleft()
        for k in range(4):
            ni, nj = x + di[k], y + dj[k]
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == -1:
                q.append((ni,nj))
                visited[ni][nj] = visited[x][y] + 1

    res = 0
    for i in range(N):
        for j in range(M):
            res += visited[i][j]
    print(f'#{tc} {res}')

