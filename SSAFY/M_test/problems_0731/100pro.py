T = int(input())

for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))

    MAX = li[N-1]
    money = 0

    for i in range(N-1, -1, -1):
        if MAX < li[i]:
            MAX = li[i]
        else:
            money += MAX - li[i]
    print(f'#{tc} {money}')
