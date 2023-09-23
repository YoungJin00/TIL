# 유기농 배추
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x, y):
    q = [(x, y)]
    MAP[x][y] = 0

    while q:
        x, y = q.pop(0)

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            if MAP[nx][ny] == 1 :
                q.append((nx,ny))
                MAP[nx][ny] = 0

T = int(input())

for tc in range(T):
    # 가로 세로 배추 위치의 개수
    M, N, K = map(int, input().split())
    cnt = 0
    # 배추 위치 x,y
    MAP = [[0]*(N) for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        MAP[x][y] = 1

    for a in range(M):
        for b in range(N):
            if MAP[a][b] == 1:
                bfs(a, b)
                cnt += 1
    print(cnt)
