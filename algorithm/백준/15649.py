# N과 M ( 1 )
# 백트래킹 활용

# def dfs():
#     if len(s) == M:
#         print(' '.join(map(str, s)))
#         return
#
#     for i in range(1, N+1):
#         if visited[i]:
#             continue
#         visited[i] = True
#         s.append(i)
#         dfs()
#         s.pop()
#         visited[i] = 0
#
#
# N, M = map(int, input().split())
# s = []
# visited = [0] * (N+1)
#
# dfs()

from itertools import permutations


N, M = map(int, input().split())

lst = list(range(1, N+1))
for i in permutations(lst, M):
    print(*i)
