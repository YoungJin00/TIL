# 격자판의 숫자 이어 붙이기

T = int(input())

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for tc in range(1, T+1):
    MAP = [list(map(int, input().split())) for _ in range(4)]

    res_set = set()
    for i in range(4):
        for j in range(4):
            stack = [(i, j, str(MAP[i][j]))]

            while stack:
                x, y, tmp = stack.pop()

                if len(tmp) == 7:
                    res_set.add(tmp)
                    continue

                for k in range(4):
                    ni, nj = x + di[k], y+dj[k]
                    if 0 <= ni < 4 and 0 <= nj < 4:
                        stack.append((ni, nj, tmp+str(MAP[ni][nj])))

    print(f'#{tc} {len(res_set)}')