'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

# 인접리스트 방법
def bfs(s, V): # 시작정점 s, 마지막정점 V
    visited = [0] * (V+1)   # visited 생성
    q = []                  # 큐 생성
    q.append(s)             # 시작점 인쿠
    visited[s] = 1          # 시작점 방문표시
    while q:                # 큐에 정점이 남아있다면
        t = q.pop(0)        # 디큐
        print(t)            # 방문한 정점에서 할일
        for i in adj[t]:
            # 인접한 정점 중 인큐되지 않은 정점찾기
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1


V, E = map(int, input().split())
lst = list(map(int, input().split()))

adj = [ [] for _ in range(V+1)]
for i in range(E):
    v1, v2 = lst[i*2], lst[i*2+1]
    adj[v1].append(v2)
    adj[v2].append(v1)

bfs(1, 7)


# 인접행렬 방법

def bfs(s, V): # 시작정점 s, 마지막정점 V
    visited = [0] * (V+1)   # visited 생성
    q = []                  # 큐 생성
    q.append(s)             # 시작점 인쿠
    visited[s] = 1          # 시작점 방문표시
    while q:                # 큐에 정점이 남아있다면
        t = q.pop(0)        # 디큐
        print(t)            # 방문한 정점에서 할일
        for i in range(1, V+1):# 인접한 정점 중 인큐되지 않은 정점찾기
            if adj[t][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1


V, E = map(int, input().split())
lst = list(map(int, input().split()))

adj = [ [0]* (V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = lst[i*2], lst[i*2+1]
    adj[v1][v2] = 1
    adj[v2][v1] = 1

bfs(1, 7)

