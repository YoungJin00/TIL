for tc in range(1, 11):
    input()
    MAP = [list(map(int, input().split())) for _ in range(100)]

    # 가로
    row_SUM = 0
    for i in range(100):
        rS = 0
        for j in range(100):
            rS += MAP[i][j]
        if row_SUM < rS:
            row_SUM = rS


    # 세로
    col_sum = 0
    for i in range(100):
        cS = 0
        for j in range(100):
            cS += MAP[j][i]
        if col_sum < cS:
            col_sum = cS

    # 대각선
    cross = 0
    cross1 = 0
    MAX_cross = 0
    MAX_cross1 = 0
    for i in range(100):
        cross += MAP[i][i]
        cross1 += MAP[i][99-i]
    if MAX_cross < cross:
        MAX_cross = cross
    if MAX_cross1 < cross1:
        MAX_cross1 = cross1

    res = max(MAX_cross, MAX_cross1, col_sum, row_SUM)

    print(f'#{tc} {res}')

