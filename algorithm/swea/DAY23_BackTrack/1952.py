# 수영장
# n월 s : n-1월까지 구입금액
def f(n, s):
    global MIN

    ## 13 이상 하는 이유는 12월에 3개월도 가능해서
    if n >= 13:
        if s < MIN:
            MIN = s
    else:
        # 1일권
        f(n+1, s+d*month[n])
        # 1개월권
        f(n+1, s+m)
        # 3개월권
        f(n+3, s+m3)


T = int(input())
for tc in range(1, T+1):
    d, m, m3, y = map(int, input().split())
    month = [0] + list(map(int, input().split()))
    MIN = y

    # 1월부터, 1월 이전 이용금액 0 원
    f(1, 0)
    print(f'#{tc} {MIN}')