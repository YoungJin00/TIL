# 최대 최소의 간격
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))
    min_idx = 0 # 최솟값의 인덱스
    max_idx = 0
    for i in range(1, N):
        if li[min_idx] > li[i]: # 작은값은 가장 먼저
            min_idx = i
        if li[max_idx] <= li[i]: # 큰값은 가장 마지막에 나오는거
            max_idx = i
    ans = max_idx - min_idx
    if ans < 0:
        ans *= -1
    print(f'#{tc} {ans}')



