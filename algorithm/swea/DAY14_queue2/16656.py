# 미로의 거리

def bfs(x, y, N):
    visited = [[0] * (N+1) for _ in range(N)]
    q = []
    q.append((x, y))
    visited[x][y] = 1
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    while q:
        x, y = q.pop(0)
        if MAP[x][y] == 3:
            return visited[x][y] -2

        for i in range(4):
            ni, nj = x + di[i], y+dj[i]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and MAP[ni][nj] != 1:
                q.append((ni, nj))
                visited[ni][nj] = visited[x][y] + 1
    return 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 2:
                ans = bfs(i, j, N)
    print(f'#{tc} {ans}')


# 강사님 풀이

# def bfs(sti, stj, N):
#     visited = [[0] * (N+1) for _ in range(N)]  # visited 생성
#     q = []                                    # 큐 생성
#     q.append((sti, stj))                     # 시작점 인큐
#     visited[sti][stj] = 1                    # 시작점 인큐 표시
#     while q:                                 # 큐가 비워질 때 까지
#         i, j = q.pop(0)                       # 디큐
#         if MAP[i][j] == 3:
#             return visited[i][j]-2           # 지나온 칸 수 리턴
#         # 인큐하고 인큐된 적이 없으면...
#         # 인큐, 인큐 표시
#         for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
#             ni, nj = i+di, j+dj
#             if 0 <= ni < N and 0 <= nj < N and MAP[ni][nj] != 1 and visited[ni][nj] == 0:
#                 q.append((ni, nj))
#                 visited[ni][nj] = visited[i][j] + 1
#     return 0                                  # 3인칸에 도달할 수 없는 경우
#
#
# def find_start(N):
#     for i in range(N):
#         for j in range(N):
#             if MAP[i][j] == 2:
#                 return i, j
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     MAP = [list(map(int, input())) for _ in range(N)]
#
#     sti, stj = find_start(N)
#     ans = bfs(sti, stj, N)
#     print(f'#{tc} {ans}')