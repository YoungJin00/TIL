# 회문2
def f(lst, N):
    MAX = 1

    for K in range(N, 1, -1):  # 큰값에서 부터 작은값 순회
        # 행, 열 순회 i, j
        for i in range(N):
            for j in range(N - K + 1):
                check = True
                for k in range(K // 2):
                    if lst[i][j + k] != lst[i][j + K - k - 1]:
                        check = False
                        break
                if check:
                    MAX = max(MAX, K)

                check = True
                for k in range(K // 2):
                    if lst[j + k][i] != lst[j + K - k - 1][i]:
                        check = False
                        break
                if check:
                    MAX = max(MAX, K)

    return MAX


T = 10
for tc in range(1, T+1):
    input()
    N = 100
    lst = [list(input()) for _ in range(N)]
    res = f(lst, N)
    print(f'#{tc} {res}')
    MAX = 1

    for k in range(N, 0, -1):
        for i in range(N):
            for j in range(N-k+1):
                for p in range(k // 2):
                    check = True
                    if lst[i][j+p] != lst[i][j+k-1-p]:
                        check = False
                        break
                if check:
                    MAX = max(MAX, k)

                for p in range(k // 2):
                    check = True
                    if lst[j+p][i] != lst[j+k-1-p][i]:
                        check = False
                        break
                if check:
                    MAX = max(MAX, k)
    print(f'#{tc} {MAX}')
