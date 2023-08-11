# 그래프 경로

def DFS(n, g, V, lst):
    stack = [] # stack 생성
    visited = [0] * (V+1) # visited 생성
    visited[n] = 1 # 시적점 방문 위치

    while True:
        for w in range(1, V+1):
            if n == g:
                return 1
            if lst[n][w] == 1 and visited[w] == 0:
                stack.append(n)
                n = w
                # print(n, end=' ')
                visited[n] = 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break
    return 0

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    adj_m = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        adj_m[a][b] = 1

    S, G = map(int, input().split())
    print(f'#{tc}', DFS(S, G, V, adj_m))