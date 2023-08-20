for tc in range(1, int(input())+1):
    N = int(input())

    MAP = [list(map(int, input().split())) for _ in range(N)]

    # max_row = 0
    #
    # for row in MAP:
    #     row_sum = 0
    #     for r in row:
    #         row_sum += r
    #     if max_row < row_sum:
    #         max_row = row_sum
    # di = [1, -1]
    # dj = [0, 0]

    di = [0, 0]
    dj = [1, -1]

    max_col = 0

    for j in range(N):
        col_sum = 0
        for i in range(N):
            col_sum += MAP[i][j]
        if col_sum > max_col:
            max_col = col_sum


    SUM = 0
    for i in range(N):
        for j in range(N):
            s = MAP[i][j]
            for k in range(2):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    s += MAP[ni][nj]
            if s - MAP[i][j] > SUM:
                SUM = s - MAP[i][j]

    result = max_col + SUM
    print(f'#{tc} {result}')