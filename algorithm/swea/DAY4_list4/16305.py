# 특별한 정렬

# def SelectionSort(a, n):
#     for i in range(n-1):
#         minIdx = i
#         maxIdx = i
#         for j in range(i+1, N):
#             if i % 2 == 1:
#                 if a[minIdx] > a[j]:
#                     minIdx = j
#             if i % 2 == 0:
#                 if a[maxIdx] < a[j]:
#                     maxIdx = j
#         a[i], a[maxIdx] = a[maxIdx], a[i]
#         a[i], a[minIdx] = a[minIdx], a[i]
#
#
#     return a
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     A = list(map(int, input().split()))
#
#     sort_A = SelectionSort(A, 5)
#
#     print(f'#{tc}', *sort_A)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = sorted(map(int, input().split()))
    sort_A = []
    # 10개만 정렬
    for i in range(5):
        sort_A.append(A[N-i-1])
        sort_A.append(A[i])
    print(f'#{tc}', *sort_A)


