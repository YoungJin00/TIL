T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min1 = arr[0]
    max2 = arr[0]
    for i in arr:
        if i > max2:
            max2 = i
        elif i < min1:
            min1 = i

    ans = max2 - min1

    print(f'#{tc} {ans}')