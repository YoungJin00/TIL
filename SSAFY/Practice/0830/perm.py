# N개 전부 나열
def f(i, N):
    if i == N:
        print(p)
        return
    else: # card[i]에 들어갈 숫자 결정
        for j in range(N):
            if used[j] == 0:
                p[i] = card[j]
                used[j] = 1
                f(i+1, N)
                used[j] = 0

card = list(map(int, input()))
used = [0] * 6
p = [0] * 6
f(0, 6)


# N개중 K개만 골라서
def f(i, N, K):  # N개에서 K개를 고르는 순열
    global cnt
    if i == K:   # 순열 완성 : K개를 모두 고른 경우
        cnt += 1
        print(cnt, p)
        return
    else: # p[i]에 들어갈 숫자 결정
        for j in range(N):
            if used[j] == 0: # 아직 사용되기 전이라면
                p[i] = card[j]
                used[j] = 1
                f(i+1, N, K)
                used[j] = 0

card = [1,2,3,4,5]
N = 5
K = 3
used = [0] * N
p = [0] * 3
cnt = 0
f(0, 5, 3)