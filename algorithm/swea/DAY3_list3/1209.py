# SUM

# for tc in range(1, 11):
#     _ = int(input())
#     num_li = [list(map(int, input().split())) for _ in range(100)]
#
#     # 각 행
#     row_max = []
#     for i in range(100):
#         row_sum = 0
#         for j in range(100):
#             row_sum += num_li[i][j]
#         row_max.append(row_sum)
#     # print(max(row_max))
#
#     # 각 열
#     col_max = []
#     for i in range(100):
#         col_sum = 0
#         for j in range(100):
#             col_sum += num_li[j][i]
#         col_max.append(col_sum)
#     # print(max(col_max))
#
#     # 대각선
#     cro_max = []
#     for i in range(100):
#         cro_sum1 = 0
#         cro_sum2 = 0
#         cro_sum1 += num_li[i][i]
#         cro_sum2 += num_li[i][100-i-1]
#         cro_max.append(max(cro_sum1, cro_sum2))
#     total = max(max(cro_max), max(col_max), max(row_max))
#     print(f'#{tc} {total}')


for t in range(1, 11):
    input()
    lst = [list(map(int ,input().split())) for _ in range(100)]
    SUM = rdia = ldia = 0

    for i in range(100):
        # print(sum(lst[i]))
        #행의 합
        # print(sum(list(zip(*lst))[i]))
        #열의 합
        rdia += lst[i][i]
        #좌에서 우로 내려가는 대각선
        ldia += lst[i][99 - i]
        #우에서 좌로 내려가는 대각선

        SUM = max(SUM, sum(lst[i]), sum(list(zip(*lst))[i]))

    result = max(SUM, rdia, ldia)


    print(f'#{t} {result}')



