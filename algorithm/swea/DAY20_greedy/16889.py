def calculate_cost(p):
    val = MAP[0][p[0]] # 첫번째 값
    for i in range(len(p) -1):
        val += MAP[p[i]][p[i+1]] # 현재에서 다음 값
    val += MAP[p[-1]][0]
    return val


def f(i, N):
    if i == N:
        val = calculate_cost(p)    # 현재 순열에 대한 값 계산
        global MIN
        MIN = min(MIN, val)        # 최소 비용
        return
    else:
        for j in range(N):
            if used[j] == 0:
                p[i] = j            # i 번째 자리에 j 배치
                used[j] = 1         # j 사용 표시
                f(i+1, N)           # 다음 자리 채우기 위해 재귀
                used[j] = 0         # 사용 표시 원복


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    used = [0] * N     # 사용여부
    p = [0] * N        # 현재 순열을 저장할 리스트 초기화
    MIN = float('inf') # 최소 비용 초기화

    f(0, N)            # 첫 번째 자리부터 시작하여 순열 생성 및 최소 비용 계산

    print(f'#{tc} {MIN}')