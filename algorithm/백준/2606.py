# 바이러스
from collections import deque

N = int(input())  # 노드
V = int(input())  # 간선

visited = [0] * (N+1) # 노드 만큼 방문 체크
g = [ [] for _ in range(N+1)]
for _ in range(V):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = 1
    cnt = 0

    while q:
        start = q.popleft()
        cnt += 1
        for i in g[start]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1

    return cnt - 1  # 본인 제외
res = bfs(1)
print(res)

'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7

'''



