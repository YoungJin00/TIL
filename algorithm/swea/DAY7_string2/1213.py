# String

for tc in range(1, 11):
    input()
    A = input()
    B = input()
    cnt = 0

    for i in range(len(B) - len(A) + 1):
        match = True
        for j in range(len(A)):
            if B[i + j] != A[j]:
                match = False
                break
        if match:
            cnt += 1

    print(f'#{tc} {cnt}')


# for tc in range(1, 11):
#     input()
#     A = input()
#     B = input()
#     cnt = 0
#
#     for i in range(len(B) - len(A) + 1):
#         for j in range(len(A)):
#             if B[i + j] != A[j]:
#                 break
#         else:
#             cnt += 1
#
#     print(f'#{tc} {cnt}')