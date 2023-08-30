def f(i, N):
    if i == N:
        print(B)
        return
    else:
        B[i] = A[i]
        f(i+1, N)

N = 5
A = [1,2,3,4,5]
B = [0] * N
f(0, N)

def f(i, N, key, arr): # i : 현재 상태, N : 목표, key : 찾고자 하는 원소
    if i == N:
        return 0
    elif arr[i] == key:
        return 1
    else:
        return f(i+1, N, key, arr)

N = 5
A = [1,2,3,4,5]
key = 13
print(f(0, N, key, A))