# 이진 탐색

def binarySearch(lst, target):
    global cnt
    low = 0
    high = len(lst) - 1
    check = 0




    while low <= high:
        mid = (low + high) // 2

        if lst[mid] == target:
            cnt += 1
            break

        elif lst[mid] < target:
            if check == 1:
                break
            low = mid + 1
            check = 1
        else:
            if check == 2:
                break
            high = mid - 1
            check = 2


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))

    cnt = 0
    for b in B:
        binarySearch(A, b)

    print(f'#{tc} {cnt}')

