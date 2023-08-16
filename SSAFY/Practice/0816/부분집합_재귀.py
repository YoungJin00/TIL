# def f(i, N):
#     if i == N:
#         print(B)
#         return
#     else:
#         B[i] = A[i]
#         f(i+1, N)
#         return
#
# N = 3
# A =[1,2,3]
# B = [0] * N
# f(0, N)

# 부분집합 재귀
def f(i, N):
    if i == N:
        s = 0
        # print(bit, end=' ')
        for j in range(N):
            if bit[j]:
                s += A[j]
                # print(A[j], end=' ')
        print(s)
        return
    else:
        bit[i] = 1
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)
        return

A = [1,2,3]
bit = [0] * 3
f(0, 3)


