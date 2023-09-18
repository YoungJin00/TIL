# 병합 정렬
T = int(input())

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst)//2
    l = lst[:mid]
    r = lst[mid:]

    l_s = merge_sort(l)
    r_s = merge_sort(r)
    return merge(l_s, r_s)


def merge(l, r):
    global cnt
    i, j = 0, 0
    sorted_lst = []
    if l[-1] > r[-1]:
        cnt += 1

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            sorted_lst.append(l[i])
            i += 1
        else:
            sorted_lst.append(r[j])
            j += 1
    while i < len(l):
        sorted_lst.append(l[i])
        i += 1
    while j < len(r):
        sorted_lst.append(r[j])
        j += 1
    return sorted_lst


for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    a = merge_sort(lst)
    # print(a)
    print(f'#{tc} {a[N//2]} {cnt}')

