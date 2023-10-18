def move(row, col, look):  # look 북(0) 서(1) 남(2) 동(3)
    for q in range(4):
        now_look = (look + q) % 4
        ni, nj = row + direction[now_look][0], col + direction[now_look][1]
        if 0 <= ni < N and 0 <= nj < N:
            if terrain[ni][nj] == 0 or terrain[ni][nj] < grow[ni][nj]:
                return (ni, nj, (now_look + 3) % 4)
    return False


T = int(input())
direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 동 북 서 남
for t in range(1, T + 1):
    N, M = map(int, input().split())
    terrain = [list(map(int, input().split())) for _ in range(N)]

    grow = [[-1] * N for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(N):
            if terrain[i][j] == 0:
                for d in range(4):  # 시작 날의 방향 정하기
                    row, col, look = i, j, d  # 초기 위치와 방향
                    temp_result = 0
                    seeds = set()
                    Kth = [[4] * N for _ in range(N)]

                    for day in range(M):
                        # seed grow
                        for seed_row, seed_col in seeds:
                            if grow[seed_row][seed_col] == -1:
                                continue
                            grow[seed_row][seed_col] += 1

                        next_move = move(row, col, look)

                        # 아침
                        if terrain[row][col] == 0:
                            if next_move:  # 식물 자라기
                                terrain[row][col] = Kth[row][col]
                                grow[row][col] = 0
                                seeds.add((row, col))
                                Kth[row][col] += 1

                        elif terrain[row][col] < grow[row][col]:
                            terrain[row][col] = 0
                            grow[row][col] = -1
                            temp_result += 1

                        # 오후
                        if next_move:
                            row, col, look = next_move

                    result = max(result, temp_result)

                    # 초기화
                    for row, col in seeds:
                        terrain[row][col] = 0
                        grow[row][col] = -1

    print(f'#{t} {result}')