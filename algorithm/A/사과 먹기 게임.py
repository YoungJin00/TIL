for t in range(1, int(input())+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    apple_loc = [[0, 0] for _ in range(11)]
    for i in range(N):
        for j in range(N):
            if MAP[i][j] != 0:
                apple_loc[MAP[i][j]] = [i, j]
    direction = 'E'
    row, col = 0, 0
    turn = 0
    idx = 0

    for lst in apple_loc[1:]:
        if lst != [0, 0]:
            idx += 1
    for i, j in apple_loc[:idx+1]:
        if row < i and col < j:
            if direction == 'E':
                turn += 1
                direction = 'S'
            elif direction == 'W':
                turn += 3
                direction = 'S'
            elif direction == 'S':
                turn += 3
                direction = 'E'
            else:
                turn += 2
                direction = 'S'

        if row < i and col > j:
            if direction == 'S':
                turn += 1
                direction = 'W'
            elif direction == 'W':
                turn += 3
                direction = 'S'
            elif direction == 'E':
                turn += 2
                direction = 'W'
            else:
                turn += 3
                direction = 'W'

        if row > i and col < j:
            if direction == 'E':
                turn += 3
                direction = 'N'
            elif direction == 'N':
                turn += 1
                direction = 'E'
            elif direction == 'W':
                turn += 2
                direction = 'E'
            else:
                turn += 3
                direction = 'E'

        if row > i and col > j:
            if direction == 'E':
                turn += 3
                direction = 'N'
            elif direction == 'N':
                turn += 3
                direction = 'W'
            elif direction == 'W':
                turn += 1
                direction = 'N'
            else:
                turn += 2
                direction = 'N'
        row, col = i, j
    print(f'#{t}', turn)