from collections import deque, defaultdict


def topological_sort(graph, inDegree):
    Q = deque()
    DP = [0 for _ in range(N+1)]

    for i in range(1, N+1):
        if inDegree[i] == 0:
            DP[i] = times[i]
            Q.append(i)

    visited = [False] * (N+1)
    visited[0] = True
    while Q:
        v = Q.popleft()
        visited[v] = True

        for i in graph[v]:
            inDegree[i] -= 1
            DP[i] = max(DP[v] + times[i], DP[i])
            if inDegree[i] == 0:
                Q.append(i)
    if not all(visited):
        DP = [-1] * (N+1)
    return DP


T = int(input())
for t in range(1, T+1):
    N = int(input())
    times = [0 for _ in range(N+1)]
    indegree = [0 for _ in range(N+1)]

    graph = defaultdict(list)
    graph2 = defaultdict(list)
    for i in range(1, N+1):
        temp = list(map(int, input().split()))
        times[i] = temp[0]
        indegree[i] = temp[1]

        for workNum in temp[2:]:
            graph[workNum].append(i)
            graph2[i].append(workNum)

    result = float('inf')
    for i in range(1, N+1):
        times[i] /= 2
        temp = topological_sort(graph, indegree[:])
        times[i] *= 2
        currMax = int(max(temp))
        if currMax == -1:
            result = -1
            break
        if currMax < result:
            result = currMax

    print(f'#{t} {result}')