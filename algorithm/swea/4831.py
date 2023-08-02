# 전기버스

"""
0번 출발 종점 N번 정류장
한번 충전 최대 이동 K
충전기 설치 M개 정류장 번호
최소한 몇번 충전 ?
"""

T = int(input())

for tc in range(1, T+1):
    # K : 한번에 갈수 있는 거리
    # N : 가야할 거리
    # M : 충전기 갯수
    K, N, M = map(int, input().split())

    # 충전기 있는 위치
    stations = list(map(int, input().split()))

    pos = 0
    cnt = 0
    next_pos = pos + K

    while next_pos < N:
        if next_pos in stations:
            cnt += 1
            pos = next_pos
            next_pos = pos + K
        else:
            next_pos -= 1

        # 충전기가 없는 경우
        if next_pos == pos:
            cnt = 0
            break
    print(f'#{tc} {cnt}')












