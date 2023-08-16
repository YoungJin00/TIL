# 순열 1
def f(i,N):
    if i == N: # 순열 완성
        print(A)

    else:
        for j in range(i, N): # 자신부터 오른쪽 끝까지
            A[i], A[j] = A[j], A[i]
            f(i+1, N)
            A[i], A[j] = A[j], A[i]  # 원상복구


A = [0,1,2]
f(0, 3)