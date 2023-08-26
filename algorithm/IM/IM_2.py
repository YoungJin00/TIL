# 사격형 그리기 게임

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    MAX = 0
    size = 0
    cnt = 0
    for i in range(N):
        for j in range(N):
            s = MAP[i][j]
            for k in range(N-1, i-1, -1):
                for l in range(N-1, j-1, -1):
                    if s == MAP[k][l]:
                        size = (k-i+1) * (l-j+1)
                        if MAX <= size:
                            if MAX < size:
                                MAX = size
                                cnt = 1
                            else:
                                cnt += 1
                        break

    print(f'#{tc} {cnt}')




