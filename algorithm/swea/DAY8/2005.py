# 파스칼의 삼각형

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[1] * n for n in range(1, N+1)]
    # print(arr)
    for i in range(1, len(arr)):
        for j in range(1, len(arr[i-1])):
            arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

    print(f'#{tc}')
    for row in arr:
        print(*row)