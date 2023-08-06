# ACM 호텔

T = int(input())

for _ in range(T):
    # 층수, 방 수, 손님
    H, W, N = map(int, input().split())
    num = N // H + 1
    floor = N % H
    # print(num, floor)
    if N % H == 0:
        num = N // H
        floor = H

    room = floor * 100 + num
    print(f'{room}')

