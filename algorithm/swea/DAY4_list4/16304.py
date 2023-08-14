# 이진 탐색
def binarySearch(N, key):
    s = 1
    cnt = 0
    while s <= N:
        mid = (s + N) // 2
        if mid == key:
           return cnt
        elif mid > key:
            N = mid
            cnt += 1
        else:
            s = mid
            cnt += 1
    return False


T = int(input())

for tc in range(1, T+1):
    # P : 전체 쪽수
    # A : A가 찾을 쪽수
    # B : B가 찾을 쪽수
    P, Pa, Pb = map(int, input().split())
    A = binarySearch(P, Pa)
    B = binarySearch(P, Pb)
    if A == B:
        w = 0
    elif A < B:
        w = 'A'
    else:
        w = 'B'

    print(f'#{tc} {w}')