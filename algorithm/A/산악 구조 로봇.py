import heapq

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dijkstra():
    heap = [(0, 0, 0)]
    INF = float('inf')
    costs = [[INF] * N for _ in range(N)]
    costs[0][0] = 0

    while heap:
        costNow, row, col = heapq.heappop(heap)

        if (row, col) == (N-1, N-1):
            return costNow

        edges = []
        for dr, dc in d:
            nr, nc = row+dr, col+dc
            if 0 <= nr < N and 0 <= nc < N:
                if terrain[nr][nc] < terrain[row][col]:
                    cost = 0
                elif terrain[nr][nc] == terrain[row][col]:
                    cost = 1
                else:
                    cost = 2 * (terrain[nr][nc] - terrain[row][col])
                edges.append((nr, nc, cost))

        if tunnels[row][col]:
            edges.extend(tunnels[row][col])

        for nr, nc, cost in edges:
            curCost = costNow + cost
            if curCost < costs[nr][nc]:
                costs[nr][nc] = curCost
                heapq.heappush(heap, (curCost, nr, nc))

    return costs[-1][-1]


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    terrain = [list(map(int, input().split())) for _ in range(N)]

    tunnels = [[[] for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        enterX, enterY, exitX, exitY, cost = map(int, input().split())
        tunnels[enterX-1][enterY-1].append((exitX-1, exitY-1, cost))
        tunnels[exitX-1][exitY-1].append((enterX-1, enterY-1, cost))

    result = dijkstra()

    print(f'#{t} {result}')