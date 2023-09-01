# 최소합
di = [0, 1]
dj = [1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    res = [[float('inf')] * N for _ in range(N)] # 최소값으로 바꿔주기 위해
    res[0][0] = MAP[0][0]                        # 스타트 값 지정

    for i in range(N):
        for j in range(N):
            for k in range(2):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    s = res[i][j] + MAP[ni][nj]
                    if res[ni][nj] > s:
                        res[ni][nj] = s
    print(f'#{tc} {res[N-1][N-1]}')

# from collections import deque
#
# di = [0, 1]
# dj = [1, 0]
#
#
# def bfs(x, y, val):
#     q = deque()
#     q.append((x,y,val))
#
#     while q:
#         x, y, val = q.popleft()
#
#         for k in range(2):
#             ni, nj = x + di[k], y+dj[k]
#
#             if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] > val+MAP[ni][nj]:
#                 visited[ni][nj] = val + MAP[ni][nj]
#                 q.append((ni, nj, val+MAP[ni][nj]))
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     MAP = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[float('inf')] * N for _ in range(N)]
#     bfs(0,0,MAP[0][0])
#     print(f'#{tc} {visited[N-1][N-1]}')


# 재귀 사용
def findMinvalue(x,y,value):
    # print(x,y,value)
    global res
    if x == N - 1 and y == N - 1: # 도착점에 도착했을때
        res = min(res, value)
        return
    if 0 <= x+1 < N:
        findMinvalue(x+1, y, value+MAP[x+1][y]) # 행 변경

    if 0 <= y+1 < N:
        findMinvalue(x, y+1, value+MAP[x][y+1]) # 열 변경


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    res = float('inf')
    findMinvalue(0,0,MAP[0][0])

    print(f'#{tc} {res}')







