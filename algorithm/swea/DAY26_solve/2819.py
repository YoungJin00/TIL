# 1. 재귀를 돌리며 숫자를 붙인다.
# 2. 숫자가 7자리가 되면
# 3. set에 넣는다


# 특정 위치를 기점으로 상하좌우 문자를 붙여야 하므로

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(y, x, num):
    if len(num) == 7:
        res.add(num)
        return

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        # 갈수 없는 위치면 continue
        if ny < 0 or ny >= 4:
            continue
        if nx < 0 or nx >= 4:
            continue

        # 갈 수 있다면, 다음 위치로 ㄱㄱ
        dfs(ny, nx, num + MAP[ny][nx])


T= int(input())

for tc in range(1, T+1):
    MAP = [input().split() for _ in range(4)]

    res = set()

    # 시작 지점 == 모두 보아야함
    for i in range(4):
        for j in range(4):
            dfs(i, j, MAP[i][j])

    print(len(res))