# 수열
N = int(input())
lst = list(map(int, input().split()))

res1 = [1] * N
res2 = [1] * N

for i in range(1, N):
    if lst[i] >= lst[i-1]:
        res1[i] = res1[i-1] + 1

    if lst[i] <= lst[i-1]:
        res2[i] = res2[i-1] + 1

MAX = max(max(res1), max(res2))
print(MAX)
