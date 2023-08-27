# 주사위 쌓기
N = int(input())

dice = []
for i in range(N):
    dice.append(list(map(int, input().split())))

DICT = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
res = []

for i in range(6):
    MAX = []
    first = [1, 2, 3, 4, 5, 6]

    bot = dice[0][i]
    top = dice[0][DICT[i]]

    first.remove(bot)
    first.remove(top)

    MAX.append(max(first))

    for j in range(1, N):
        next = [1,2,3,4,5,6]
        bot = top
        top_idx = DICT[dice[j].index(top)]
        top = dice[j][top_idx]

        next.remove(bot)
        next.remove(top)

        MAX.append(max(next))

    res.append(sum(MAX))
print(max(res))
