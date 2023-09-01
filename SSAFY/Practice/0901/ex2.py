T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    cnt = 0
    for i in range(1 << N):
        s = 0
        for j in range(N):
            if i & (1<<j):
                s += lst[j]

        if s == K:
            cnt += 1
    print(f'#{tc} {cnt}')

def f(i, N, s, K):
    global cnt
    if i == N:
        if s ==K:
            cnt += 1
    else:
        f(i+1, N, s+lst[i], K)
        f(i+1, N, s, K)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    f(0,N,0,K)
    print(f'#{tc} {cnt}')

