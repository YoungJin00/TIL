# 장훈이의 높은 선반

from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    # N : 점원수 S: 점원들 키 합
    N, B = map(int, input().split())
    # H 의 합이 B이상이면서 차이가 가장 작은 것 출력
    H = list(map(int, input().split()))

    res = float('inf')
    for i in range(1, N+1):
        for j in combinations(H, i):
            # print(j)
            SUM = sum(j)
            if SUM >= B:
                diff = SUM - B
                if res > diff:
                    res = diff

    print(f'#{tc} {res}')