# 단지번호붙이기
import sys
input = sys.stdin.readline

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def dfs(x,y):
    cnt = 1
    for k in range(4):
        ni, nj = x+di[k], y+dj[k]
        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            continue
        # 처음 방문
        if g[ni][nj] == 1:
            g[ni][nj] = -1
            cnt += dfs(ni, nj)
    return cnt


N = int(input())
g = [[0]*N for _ in range(N)]

for i in range(N):
    tmp = input()
    for j in range(N):
        g[i][j] = int(tmp[j])
# print(g)

res = []
for i in range(N):
    for j in range(N):
        if g[i][j] == 1:
            g[i][j] = -1
            res.append(dfs(i,j))
res.sort()
print(len(res))
for i in res:
    print(i)




