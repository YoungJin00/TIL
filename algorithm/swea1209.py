for tc in range(1, 11):
    _ = int(input())
    bingo = [list(map(int, input().split())) for _ in range(100)]

  # 각 행
    row_max = []
    for i in range(100):
        row_sum = 0
        for j in range(100):            
            row_sum += bingo[i][j]
        row_max.append(row_sum)

  # 각 열
    col_max = []
    for i in range(100):
        col_sum = 0
        for j in range(100):
            col_sum += bingo[j][i]
        col_max.append(col_sum)

  # 대각선
    cro_max = []
    cro_sum1 = 0
    cro_sum2 = 0
    for i in range(100):
        cro_sum1 += bingo[i][i]
        cro_sum2 += bingo[i][99-i]
    cro_max.append(max(cro_sum1, cro_sum2))
                       
    print(f'#{tc} {max(max(row_max), max(col_max), max(cro_max))}')