for tc in range(1, 11):
    N = int(input())
    dump = list(map(int, input().split()))

    ans = 0
    while N > 0:
        N -= 1
        max_idx = 0
        min_idx = 0
        for i in range(1, 100):
            if dump[min_idx] > dump[i]: # 가장 낮은곳
                min_idx = i
            if dump[max_idx] < dump[i]: # 가장 높은 곳
                max_idx = i
        if dump[max_idx] - dump[min_idx] < 2:
            ans = dump[max_idx] - dump[min_idx]
            break
        else:
            dump[max_idx] -= 1
            dump[min_idx] += 1
    if N == 0 :
        max_idx = 0
        min_idx = 0
        for i in range(100):
            if dump[min_idx] > dump[i]:  # 가장 낮은곳
                min_idx = i
            if dump[max_idx] < dump[i]:  # 가장 높은 곳
                max_idx = i

        ans = dump[max_idx] - dump[min_idx]

    print(f'#{tc} {ans}')


