# 알고리즘 수업 - 깊이 우선 탐색 1
import sys
sys.setrecursionlimit(15000000)

def dfs(r):
    global cnt
    visited[r] = cnt
    g[r].sort()
    for i in g[r]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

N, M, R = map(int, input().split())
cnt = 1
visited = [0] * (N+1)
g = [ [] for _ in range(N+1)]
for _ in range(N):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

dfs(R)
for i in range(1, N+1):
    print(visited[i])