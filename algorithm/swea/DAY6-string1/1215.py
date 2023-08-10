# 회문 1

for tc in range(1, 11):
    N = int(input())
    MAP = [input() for _ in range(8)]
    # print(MAP)

    # 가로
    row_cnt = 0
    for i in range(8):
        for j in range(8-N+1):
            s = MAP[i][j:j+N]
            if s == s[::-1]:
                row_cnt += 1
    # print(row_cnt)

    # 세로
    li = []
    for j in range(8 -N +1):
        for i in range(8):
            s = ''.join(MAP[j+x][i] for x in range(N))
            li.append(s)
    col_cnt = 0
    for i in range(len(li)):
        if li[i] == li[i][::-1]:
            col_cnt += 1

    res = row_cnt + col_cnt
    print(f'#{tc} {res}')



for i in range(2):
    for j in range(2):
        for k in range(2):
            print(i, j, k)










