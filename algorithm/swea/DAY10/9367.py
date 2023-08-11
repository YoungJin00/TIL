# 점점 커지는 당근의 개수

for tc in range(1, int(input())+1):
    N = int(input())
    C = list(map(int, input().split()))
    res = 1
    cnt = 1

    for i in range(1, N):
        if C[i] > C[i-1]:
            cnt += 1
            if res < cnt:
                res = cnt
        else:
            cnt = 1

    print(f'#{tc} {res}')