def cut(lst, K, key):
    cnt = 0
    for i in lst:
        cnt += i // key
    return cnt >= K


def binary_search(lst, K):
    s, e = 1, max(lst)
    res = 0

    while s <= e:
        mid = (s+e) // 2
        if cut(lst, K, mid):
            res = mid
            s = mid + 1
        else:
            e = mid - 1
    return res


N, K = map(int, input().split())

lst = [int(input()) for _ in range(N)]
ans = binary_search(lst, K)
print(ans)