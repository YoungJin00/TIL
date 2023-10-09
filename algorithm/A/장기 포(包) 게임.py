def is_valid(arr, i, j, ni, nj):
    enemy = 0
    result = []

    if ni == i:
        step = 1 if nj > j else -1
        for col in range(j + step, nj, step):
            if 0 <= col < N:
                if enemy == 1:
                    result.append((i, col))
                enemy += arr[i][col]
                if enemy >= 2:
                    return result

    elif nj == j:
        step = 1 if ni > i else -1
        for row in range(i + step, ni, step):
            if 0 <= row < N:
                if enemy == 1:
                    result.append((row, j))
                enemy += arr[row][j]
                if enemy >= 2:
                    return result

    return result


def cannon(arr, i, j, time=0):
    if time == 4:
        return
    if (i, j, time) in visited:
        return
    visited.add((i, j, time))
    if arr[i][j] == 1:
        kill_list.add((i, j))
        arr[i][j] = 0
        next_move(arr, i, j, time)
        arr[i][j] = 1
    else:
        next_move(arr, i, j, time)


def next_move(arr, i, j, time):
    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ni, nj = i + di*N, j + dj*N
        valid_list = is_valid(arr, i, j, ni, nj)
        if valid_list:
            for row, col in valid_list:
                cannon(arr, row, col, time+1)


for t in range(1,int(input())+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    kill_list = set()
    visited = set()
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                board[i][j] = 0
                cannon(board, i, j)
                break

    print(f'#{t}', len(kill_list))