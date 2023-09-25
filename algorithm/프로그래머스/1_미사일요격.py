def solution(targets):
    if not targets:
        return 0

    # end 기준으로 정렬
    targets.sort(key=lambda x: x[1])

    # 미사일 수
    cnt = 0
    # 현재 범위
    now = float('-inf')

    for target in targets:
        start, end = target
        # start가 now랑 겹치는 부분이 없다면 횟수 증가
        if start >= now:
            cnt += 1
            now = end

    return cnt