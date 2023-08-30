from collections import deque

N, M, V = map(int, input().split())
g = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a][b] = 1
    g[b][a] = 1

visited1 = [0] * (N+1)
visited2 = [0] * (N+1)

def bfs(V):
    q = deque()
    q.append(V)
    visited2[V] = 1
    while q:
        V = q.popleft()
        print(V, end=' ')
        for i in range(1, N+1):
            if not visited2[i] and g[V][i]:
                q.append(i)
                visited2[i] = 1

def dfs(V):
    visited1[V] = 1
    print(V, end=' ')
    for i in range(1, N+1):
        if not visited1[i] and g[V][i]:
            dfs(i)

dfs(V)
print()
bfs(V)



