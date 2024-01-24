def hexa_search(visited):
    global MAX
    check = tuple(sorted(visited))
    if check in dup:
        return
    else:
        dup.add(check)

    result = sum(MAP[row][col] for row, col in visited)

    if result + (4-len(visited)) * max_val < MAX:
        return

    if len(visited) == 4:
        MAX = max(MAX, result)
        return

    for i, j in visited:
        if j % 2 == 1:
            d = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1]]
        else:
            d = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, 1], [-1, -1]]

        for di, dj in d:
            ni, nj = i+di, j+dj
            if 0 <= ni < H and 0 <= nj < W and (ni, nj) not in visited:
                hexa_search(visited | {(ni, nj)})


for t in range(1, int(input())+1):
    H, W = list(map(int, input().split()))
    MAP = [list(map(int, input().split())) for _ in range(H)]
    max_val = max(max(row) for row in MAP)
    MAX = 0
    dup = set()
    for x in range(H):
        for y in range(W):
            if (x+y) % 2 == 0:
                hexa_search({(x, y)})

    print(f'#{t}', MAX)
    
    
    
    
# 2
T = int(input())


def dfs(i, j, move, total, visited, lst):
    # global
    global max_honey

    # 백트래킹
    if total + (4 - move) * 10000000 <= max_honey:
        return

    # 종료 조건
    if move == 4:
        max_honey = max(max_honey, total)
        return

    # 수행 동작
    if j % 2 == 0:
        deltas = even_deltas
    else:
        deltas = odd_deltas

    for di, dj in deltas:
        ni = i + di
        nj = j + dj

        if 0 <= ni < N and 0 <= nj < M and (ni, nj) not in visited:
            visited.append((ni, nj))
            dfs(ni, nj, move + 1, total + lst[ni][nj], visited, lst)
            visited.remove((ni, nj))

def bfs(i, j, move, total, visited, lst):
    # global
    global max_honey

    # 백트래킹
    if total + (4 - move) * 10000000 <= max_honey:
        return

    # 종료 조건
    if move == 4:
        max_honey = max(max_honey, total)
        return

    # 수행 동작
    if j % 2 == 0:
        deltas = even_deltas
    else:
        deltas = odd_deltas

    for di, dj in deltas:
        ni = i + di
        nj = j + dj

        if 0 <= ni < N and 0 <= nj < M and (ni, nj) not in visited:
            visited.append((ni, nj))
            bfs(i, j, move + 1, total + lst[ni][nj], visited, lst)
            visited.remove((ni, nj))

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    honeycomb = []
    for _ in range(N):
        honeycomb.append(list(map(int, input().split())))
    odd_deltas = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1)]
    even_deltas = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1)]
    max_honey = 0
    for i in range(N):
        for j in range(M):
            dfs(i, j, 1, honeycomb[i][j], [(i, j)], honeycomb)
            bfs(i, j, 1, honeycomb[i][j], [(i, j)], honeycomb)

    print(f"#{tc} {max_honey}")