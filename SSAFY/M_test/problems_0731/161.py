T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())  # N = 행 개수 / M = 열 개수
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    # 오른쪽, 아래, 왼쪽, 위
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    sum_idx = 0
    for i in range(N):
        for j in range(M):
            point = arr[i][j]
            for k in range(4):
                for l in range(1, arr[i][j] + 1):
                    ai = i + di[k] * l
                    aj = j + dj[k] * l
                    if 0 <= ai < N and 0 <= aj < N:
                        point += arr[ai][aj]
            if sum_idx < point:
                sum_idx = point

    print(f'#{tc} {sum_idx}')