import sys
input = sys.stdin.readline
# 재귀 제한 변경
sys.setrecursionlimit(int(1e5))

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def dfs(i,j):
    for k in range(4):
        ni, nj = i + di[k], j+dj[k]
        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            continue
        if not visited[ni][nj]:
            if g[i][j] == g[ni][nj]:
                visited[ni][nj] = -1
                dfs(ni, nj)


N = int(input())
g = [[] for _ in range(N)]
for i in range(N):
    for j in input():
        g[i].append(j)


# 기본
res = 0
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        # 처음 방문하는 경우
        if not visited[i][j]:
            visited[i][j] = 1
            dfs(i, j)
            res += 1
print(res, end=' ')

#적녹
res = 0
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if g[i][j] == 'R':
            g[i][j] = 'G'

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = 1
            dfs(i, j)
            res += 1
print(res)





