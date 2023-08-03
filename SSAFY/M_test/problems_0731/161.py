for tc in range(1, 11):
    _ = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 상 우 좌
    di = [-1, 0, 0]
    dj = [0, 1, -1]
    direct  = 0



    for i in range(100):
        if ladder[99][i] == 2:
            # 출발 열
            y = i
            break
    # 출발 행
    x = 99
    while x > 0:
        # 왼쪽으로 이동
        if y > 0 and ladder[x][y-1] == 1:
            while y > 0 and ladder[x][y-1] == 1:
                y += 1

        # 오른쪽으로 이동
        if y > 0 and ladder[x][y+1] == 1:
            while y > 0 and ladder[x][y+1] == 1:
                y += 1

        x -= 1

        print(f'#{tc} {y}')





