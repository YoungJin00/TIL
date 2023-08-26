# 1970 쉬운 거스름돈
'''
2
32850
160
'''
change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lst = [0] * 8

    for i in range(8):
        if n >= change[i]:
            lst[i] = n // change[i]
            n %= change[i]

    print(f'#{tc}', end=' ')
    print(*lst)