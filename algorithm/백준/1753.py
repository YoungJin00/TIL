# 최단경로
import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    pq = []
    heapq.heappush(pq, [0, start])
    distances[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if distances[now] < dist:
            continue

        for next_node, cost in g[now]:
            new_cost = dist + cost

            if distances[next_node] <= new_cost:
                continue

            distances[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))


V, E = map(int, input().split())
K = int(input())  # 시작 정점

g = [[] for _ in range(V+1)]
distances = [99999999] * (V+1)

for _ in range(E):
    f, t, w = map(int, input().split())
    g[f].append([t, w])

dijkstra(K)
for i in distances[1:]:
    if i == 99999999:
        print('INF')

    else:
        print(i)
