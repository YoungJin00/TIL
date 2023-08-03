# 부분집합의 합

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    n = len(A)
    li_sum = []
    res = 0
    for i in range(1 << n):
        li = []
        for j in range(n):
            if i & (1 << j):
                li.append(A[j])
        if len(li) == N:
            li_sum.append(li)
    for l in li_sum:
        if sum(l) == K:
            res += 1
    print(f'#{tc} {res}')



