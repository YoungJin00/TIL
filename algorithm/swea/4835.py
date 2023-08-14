# 구간합 16101
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     li = list(map(int, input().split()))
#     max1 = sum(li[0:M])
#     min1 = sum(li[0:M])
#     for i in range(N-M+1):
#         res = sum(li[i:i+M])
#         if res > max1:
#             max1 = res
#         elif res < min1:
#             min1 = res
#     print(f'#{tc} {max1 - min1}')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    MAX = 0
    # 얘보다 작으면 바꿔주기 위함
    MIN = 999999
    ans = 0

    for i in range(N - M +1):
        SUM = li[i]

        for j in range(i+1, i + M):
            SUM += li[i]

        if SUM > MAX:
            MAX = SUM
        if SUM < MIN:
            MIN = SUM
    ans = MAX - MIN
    print(f'#{tc} {ans}')