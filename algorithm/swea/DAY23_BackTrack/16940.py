# 퀵 정렬
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    l = [x for x in lst if x < pivot]
    r = [x for x in lst if x > pivot]
    m = [x for x in lst if x == pivot]

    return quick_sort(l) + m + quick_sort(r)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    a = quick_sort(lst)
    print(f'#{tc} {a[N//2]}')