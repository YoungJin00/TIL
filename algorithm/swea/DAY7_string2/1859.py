
# 백만 장자

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    day = list(map(int, input().split()))

    MAX = day[N-1]
    money = 0

    for i in range(N-2, -1, -1):
        if day[i] > MAX:
            MAX = day[i]
        else:
            money += MAX - day[i]

    print(f'#{tc} {money}')