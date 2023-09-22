# def dfs(start):
#     if len(s) == M:
#         print(' '.join(map(str, s)))
#         return
#
#     for i in range(start, N+1):
#         if visited[i]:
#             continue
#         visited[i] = True
#         s.append(i)
#         dfs(i+1)
#         s.pop()
#         visited[i] = 0
#
#
# N, M = map(int, input().split())
# s = []
# visited = [0] * (N+1)
#
#
# dfs(1)

from itertools import combinations


N, M = map(int, input().split())

lst = list(range(1, N+1))
for i in combinations(lst, M):
    print(*i)