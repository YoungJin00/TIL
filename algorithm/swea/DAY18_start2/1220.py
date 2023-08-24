# magnetic
T = 10
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(100)]

    cnt = 0
    for i in range(N):
        north = 0
        for j in range(N):
            if MAP[j][i] == 1:
                north = 1
            elif MAP[j][i] == 2 and north:
                cnt += 1
                north = 0

    print(f'#{tc} {cnt}')