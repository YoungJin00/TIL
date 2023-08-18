# 노드의 거리

def bfs(s, e):
    visited = [0] * (V+1)
    q = []
    q.append(s)
    # visited[s] = 1
    while q:
        s = q.pop(0)
        if s == e:
            return visited[s]
        for i in g[s]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[s] + 1
    return 0

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split()) # 6 5

    g = [[] for _ in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    S, G = map(int, input().split())
    ans = bfs(S, G)

    print(f'#{tc} {ans}')

