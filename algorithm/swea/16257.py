# 색칠하기

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [[0] * 10 for _ in range(10)]
    res = 0
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        # print(r1, c1, r2, c2, color)
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                lst[i][j] += color
                if lst[i][j] == 3:
                    res += 1
    print(f'#{tc} {res}')

for tc in range(1, T+1):
    area = [[0 for _ in range(10)] for _ in range(10)]
    count = 0
    N = int(input())

    for i in range(1, N+1):
        r1, c1, r2, c2, color = map(int, input().split())

        for row in range(r1, r2+1):
            for col in range(c1, c2+1):
                if color == 1:
                    if area[row][col] == 0:
                        area[row][col] =1

                    elif area[row][col] == 2:
                        area[row][col] = 3
                        count += 1
                else:
                    if area[row][col] == 0:
                        area[row][col] = 2
                    elif area[row][col] == 1:
                        area[row][col] =3
                        count += 1
    print(f'#{tc} {count}')




