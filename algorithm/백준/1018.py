# 체스판 다시 칠하기

N, M = map(int, input().split())
chess_map = [input() for _ in range(N)]
cnt = []
for i in range(N-7):
    for j in range(M-7):
        w_inx = 0
        b_idx = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2 == 0:
                    if chess_map[k][l] != 'W':
                        w_inx += 1
                    if chess_map[k][l] != 'B':
                        b_idx += 1
                else:
                    if chess_map[k][l] != 'B':
                        w_inx += 1
                    if chess_map[k][l] != 'W':
                        b_idx += 1

        cnt.append(min(w_inx, b_idx))
print(min(cnt))

