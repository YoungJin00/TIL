'''
주어진 도시들과 도시 간의 도로 정보 바탕으로 특정 출발도시에서부터 특정거리 만큼 떨어진 도시들을 찾는 문제
'''
import sys

def DFS(x, d): # 출발 도시, 거리
    visited[x] = True # 현재 방문 도시
    if d == K:
        stack.append(x) # 도착 후 추가
        return
    for n in MAP[x]:
        if not visited[n]: # 방문하지 않았다면
            DFS(n, d+1) # 옆도시로 호출

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
