# 미로 2
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(i, j):
    visited = [[0] * 101 for _ in range(101)]
    q = [(i, j)]
    visited[i][j] = 1

    while q:
        i, j = q.pop(0)

        if MAP[i][j] == 3:
            return 1

        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < 100 and 0 <= nj < 100 and visited[ni][nj] == 0 and MAP[ni][nj] != 1:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0


for tc in range(1, 11):
    input()
    MAP = [list(map(int, input())) for _ in range(100)]

    for i in range(100):
        for j in range(100):
            if MAP[i][j] == 2:
                ans = bfs(i, j)

    print(f'#{tc} {ans}')