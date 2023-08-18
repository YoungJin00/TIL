# 미로 1

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(i, j):
    visited = [ [0] * 17 for _ in range(17)]
    q = [(i, j)]
    visited[i][j] = 1

    while q:
        i, j = q.pop(0)

        if MAP[i][j] == 2:
            return 1

        for k in range(4):
            ni, nj = i + di[k], j+ dj[k]
            if 0 <= ni < 16 and 0 <= nj < 16 and MAP[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0


for tc in range(1, 11):
    input()
    MAP = [list(map(int, input())) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if MAP[i][j] == 3:
                ans = bfs(i, j)

    print(f'#{tc} {ans}')