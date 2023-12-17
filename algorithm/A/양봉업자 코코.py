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