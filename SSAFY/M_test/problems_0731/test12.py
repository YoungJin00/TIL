for tc in range(1, 11):
    _ = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if ladder[99][i] == 2:
            # 출발 열
            col = i
            break
    # 출발 행
    row = 99

    while row > 0:
        # 왼쪽 이동
        if col > 0 and ladder[row][col-1] == 1:
            while col > 0 and ladder[row][col-1] == 1:
                col -= 1

        # 오른쪽 이동
        elif col < 99 and ladder[row][col+1] == 1:
            while col < 99 and ladder[row][col+1] == 1:
                col += 1
        # 위로 이동
        row -= 1

    print(f'#{tc} {col}')