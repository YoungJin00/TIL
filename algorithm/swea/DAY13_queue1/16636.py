# 회전 문제 (회전)

t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    ls = []
    for i in range(M % N):
        lst.remove(lst[0])

    print(f'#{tc} {lst[0]}')