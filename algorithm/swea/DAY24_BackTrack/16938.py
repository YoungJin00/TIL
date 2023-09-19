# 최소 생산 비용
def dfs(n, total):
    global MIN
    if n == N:
        MIN = min(MIN, total)
        return
    if total > MIN:
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            new_total = total + cost[n][i]
            dfs(n+1, new_total)
            visited[i] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    MIN = float('inf')
    dfs(0, 0)

    print(f'#{tc} {MIN}')

