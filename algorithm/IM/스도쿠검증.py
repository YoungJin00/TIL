T = int(input())
for tc in range(1, T+1):
    MAP = [list(map(int, input().split())) for _ in range(9)]

    # 가로
    row_MAP = MAP

    # 세로
    col_MAP = []
    for j in range(9):
        col = []
        for i in range(9):
            col.append(MAP[i][j])
        col_MAP.append(col)


    # 3 X 3
    tt_MAP = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            tt = []
            for x in range(i, i+3):
                for y in range(j, j+3):
                    tt.append(MAP[x][y])
            tt_MAP.append(tt)


    res = 0
    for i in range(9):
        if len(set(row_MAP[i])) == len(set(col_MAP[i])) == len(set(tt_MAP[i])) == 9:
            res = 1
        else:
            res = 0
            break

    print(f'#{tc} {res}')





