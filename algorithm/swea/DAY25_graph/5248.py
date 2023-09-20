# 그룹나누기
def dfs(s):
    q = [s]
    visited[s] = 1

    while q:
        now = q.pop()

        for next in graph[now]:
            if visited[next] == 1:
                continue
            if visited[next] == 0:
                dfs(next)


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    graph = [ [] for _ in range(N+1)]
    visited = [0] * (N+1)

    for i in range(M):
        a, b = lst[i*2], lst[i*2+1]
        graph[a].append(b)
        graph[b].append(a)

    cnt = 0
    for i in range(1, N+1):
        if visited[i] == 0: # 방문하지 않은 노드인 경우에만 값 증가
            cnt += 1
            dfs(i)

    print(f'#{tc} {cnt}')


def dfs(v):
    visited[v] = 1
    for next in range(len(graph[v])):
        to = graph[v][next]
        if visited[to]:
            continue
        dfs(to)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N = 출석번호, M = 신청서 의 개수
    numbers = list(map(int, input().split()))

    graph = [[] for _ in range(N+1)]
    # print(graph)
    for i in range(M):
        v1 = numbers[i*2]
        v2 = numbers[i*2 + 1]
        graph[v1].append(v2)
        graph[v2].append(v1)
    visited = [0] * (N+1)
    cnt = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            cnt += 1
            dfs(i)

    print(f'#{tc} {cnt}')

    
    
    
# def find_set(x):
#     if parent[x] == x:
#         return x
#     parent[x] = find_set(parent[x])
#     return parent[x]
#
# def union(x, y, rank):
#     x_root = find_set(x)
#     y_root = find_set(y)
#
#     if x_root != y_root:
#         if rank[x_root] > rank[y_root]:
#             parent[y_root] = x_root
#         else:
#             parent[x_root] = y_root
#             if rank[x_root] == rank[y_root]:
#                 rank[y_root] += 1
#
# # 입력 처리
# T = int(input())
# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#     groups = list(map(int, input().split()))
#     parent = list(range(N + 1))  # 각 원소의 부모를 자기 자신으로 초기화
#     rank = [0] * (N + 1)
#
#     # 각 그룹의 대표 원소를 찾아서 합치기
#     for i in range(0, M * 2, 2):
#         x, y = groups[i], groups[i + 1]
#         union(x, y, rank)
#
#     # 서로소 집합의 개수 세기
#     unique_sets = set()
#     for i in range(1, N + 1):
#         unique_sets.add(find_set(i))
#
#     answer = len(unique_sets)
#     print(f"#{test_case} {answer}")
