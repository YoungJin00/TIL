# 컨테이너 운반
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())   # N 컨테이너수, M 트럭 수
    w = sorted(map(int, input().split()), reverse= True)
    t = sorted(map(int, input().split()), reverse= True)

    con = [0] * M

    for i in range(M):
        for j in range(N):
            if t[i] >= w[j]:
                con[i] = w[j]
                w[j] = float('inf')
                break
    res = sum(con)
    print(f'#{tc} {res}')