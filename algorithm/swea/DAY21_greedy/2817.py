# 부분 수열의 합
def subset(i, N, K):
    global cnt
    if i == N:
        s = 0
        for j in range(N):
            if bit[j]:
                s += lst[j]
        if s == K:
            cnt += 1
    else:
        bit[i] = 1
        subset(i+1, N, K)
        bit[i] = 0
        subset(i+1, N, K)


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    bit = [0] * N
    cnt = 0
    subset(0, N, K)
    print(f'#{tc} {cnt}')