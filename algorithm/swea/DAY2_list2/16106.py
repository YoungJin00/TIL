# 전기 버스
T = int(input())

for tc in range(1, T + 1):
    # K : 한번 충전으로 최대한 이동할 수 있는 정류장 수
    # N : 종점 정류장
    # M : 충전기가 설치된 정류장 개수
    K, N, M = map(int, input().split())
    ch = list(map(int, input().split()))

    pos = 0  # 현재 위치
    charge_count = 0  # 충전 횟수

    while pos + K < N:  # 목적지에 도착할 때까지 반복
        for j in range(K, 0, -1):  # 현재 위치에서 최대 이동 가능 거리 K부터 1씩 감소하면서 확인
            if (pos + j) in ch:  # 다음 정류장이 목적지이거나 충전기가 있을 경우 이동 가능
                pos += j
                charge_count += 1
                break
        else:  # for문이 break 없이 종료되었을 때 (이동 불가능한 상황)
            charge_count = 0
            break

    print(f'#{tc} {charge_count}')