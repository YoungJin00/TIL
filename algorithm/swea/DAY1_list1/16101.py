
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    max1 = sum(li[0:M])
    min1 = sum(li[0:M])
    for i in range(N-M+1):
        res = sum(li[i:i+M])
        if res > max1:
            max1 = res
        elif res < min1:
            min1 = res
    print(f'#{tc} {max1 - min1}')