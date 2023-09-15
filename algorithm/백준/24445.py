from collections import deque
import sys
input = sys.stdin.readline
def bfs(r):
    global cnt
    q = deque([R])
    visited[R] = 1

    while q:
        r = q.popleft()
        g[r].sort(reverse=True)
        for i in g[r]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                q.append(i)


N, M, R = map(int, input().split())

g = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1
for _ in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

bfs(R)
for i in visited[1:]:
    print(i)
