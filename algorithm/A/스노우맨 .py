import heapq


def dijkstra(row, col):
    heapQ = [(0, row, col)]
    costs = [[float('inf')] * M for _ in range(N)]
    costs[row][col] = 0
    result = 0

    while heapQ:
        costNow, i, j = heapq.heappop(heapQ)

        if costNow > costs[i][j]:
            continue

        result = max(result, costNow)
        if MAP[i][j] == 3:
            return result

        elif MAP[i][j] != 0:
            costNow = 0

        for k in range(4):
            ni, nj = i+d[k][0], j+d[k][1]
            if 0 <= ni < N and 0 <= nj < M:
                if k < 2:
                    cost = costNow + 1

                    if cost < costs[ni][nj]:
                        costs[ni][nj] = cost
                        heapq.heappush(heapQ, (cost, ni, nj))

                elif MAP[i][j] != 0 and MAP[ni][nj] != 0:
                    cost = costNow

                    if cost < costs[ni][nj]:
                        costs[ni][nj] = cost
                        heapq.heappush(heapQ, (cost, ni, nj))


d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if MAP[i][j] == 2:
            result = dijkstra(i, j)
            break
    else:
        continue
    break

print(result)