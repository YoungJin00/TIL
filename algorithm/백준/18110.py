import sys
input = sys.stdin.readline
N = int(input())

def f(n):
    if n == int(n):
        return int(n)
    else:
        if n - int(n) >= 0.5:
            return int(n) + 1
        else:
            return int(n)

if not N:
    print(0)
else:
    n_lst = [int(input()) for _ in range(N)]
    n_lst.sort()
    n_del = f(N * 0.15)

    cnt = N - 2 * n_del
    if n_del != 0:
        n_lst = n_lst[n_del:-n_del]
    res = sum(n_lst)
    # res = 0
    # for i in range(n_del, N-n_del):
    #     res += n_lst[i]

    print(f(res/cnt))








