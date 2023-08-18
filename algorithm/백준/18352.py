'''
주어진 도시들과 도시 간의 도로 정보 바탕으로 특정 출발도시에서부터 특정거리 만큼 떨어진 도시들을 찾는 문제
'''
# DFS로 풀었으나 못품
import sys

def DFS(x, d): # 출발 도시, 거리
    visited = [0] * (N+1)
    q = [s]
    visited[s] = 1
    res = []
    while q:
        s = q.pop(0)

        for i in MAP[s]:
            if not visited[i]:
                visited[i] = visited[s] + 1
                q.append(i)
                if visited[i] == d + 1: # 출발 도시까지 거리가 1부터 K거리 까지 도달하려면 k+1되어야함
                    res.append(i)
    return res


# 도시 수, 도로 수, 목표거리, 출발 도시
N, M, K, X = map(int, sys.stdin.readline().split())
MAP = [ [] for _ in range(N+1)] # 도시 간의 도로 정보 저장

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    MAP[a].append(b) # a > b 도로 추가

visited = [False] * (N+1) # 도시 방문 여부를 저장할 리스트 초기화
stack = [] # 스택 리스트 초기화

DFS(X, 0)

if not stack:
    print(-1)
else:
    stack.sort()
    for city in stack:
        print(city)

# 시간 초과 뜸
# import sys
# input = sys.stdin.readline

# def bfs(s, k):
    # visited = [0] * (N+1)
    # q = [s]
    # visited[s] = 1
    # res = []
    # while q:
    #     s = q.pop(0)

    #     for i in MAP[s]:
    #         if not visited[i]:
    #             visited[i] = visited[s] + 1
    #             q.append(i)
    #             if visited[i] == k + 1: # 출발 도시까지 거리가 1부터 K거리 까지 도달하려면 k+1되어야함
    #                 res.append(i)
    # return res


# N, M, K, X = list(map(int, input().split()))
# MAP = [[] for _ in range(N+1)]

# for _ in range(M):
#     s, e = map(int, input().split())
#     MAP[s].append(e)

# ans = bfs(X, K)
# ans.sort()
# if not ans:
#     print(-1)
# else:
#     for city in ans:
#         print(city)


# 패스한 문제
import sys
from collections import deque

input = sys.stdin.readline

def bfs(s, k):
    visited = [0] * (N+1)
    q = deque([s])
    visited[s] = 1
    res = []
    while q:
        s = q.popleft()  # Use popleft() instead of pop(0)

        for i in MAP[s]:
            if not visited[i]:
                visited[i] = visited[s] + 1
                q.append(i)
                if visited[i] == k + 1:
                    res.append(i)
    return res

N, M, K, X = list(map(int, input().split()))
MAP = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    MAP[s].append(e)

ans = bfs(X, K)
ans.sort()
if not ans:
    print(-1)
else:
    for city in ans:
        print(city)