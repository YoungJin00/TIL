# 부분집합의 합  연습문제

def f(i, N, s):
    if i == N:
        if s == 10:
            for j in range(N):
                if bit[j]:
                    print(A[j], end=' ')
            print(bit)
        return
    else:
        bit[i] = 1
        f(i+1, N, s+A[i])
        bit[i] = 0
        f(i+1, N, s)
        return

# 1부터 10까지 원소인 집합에서 부분집합의 합이 10인 경우는?
N = 10
A = [i for i in range(1, N+1)]
bit = [0] * N
f(0, N, 0)

# 가지치기
def f(i, N, s , t): # s: 1-i원소까지 부분집합의 합, t: 찾으려는 합
    global cnt
    cnt += 1
    if s == t: # 찾는 합이 목표치에 도달했으면
        for j in range(N):
            if bit[j]:
                print(A[j], end=' ')
        print(bit)
        return
    elif i == N:
        return
    elif s > t:
        return
    else:
        bit[i] = 1
        f(i+1, N, s+A[i], t)
        bit[i] = 0
        f(i+1, N, s, t)
        return

# 1부터 10까지 원소인 집합에서 부분집합의 합이 10인 경우는?
N = 10
A = [i for i in range(1, N+1)]
bit = [0] * N
cnt = 0
f(0, N, 0, 10)
print(cnt)