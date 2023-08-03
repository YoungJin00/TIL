# 달팽이 숫자

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    # 우 하 좌 상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # 초기위치 & 방향 설정
    r = c = 0
    dist = 0

    for i in range(1, N*N +1):
        arr[r][c] = i
        r += di[dist]
        c += dj[dist]
        # 범위 벗어나거나 0이 아닌 다른 값이 있다면, dist 방향 체인지
        # 근데 이런 경우라면 요소 인덱스를 다시 원위치 시켜줘야하므로 뺴줘야함
        # 그런다음 dist의 방향을 바꾸고, 방향 바꿨으면 다시 움직이기
        if r < 0 or c < 0 or r >= N or c >= N or arr[r][c] != 0:
            # 실행취소
            r -= di[dist]
            c -= dj[dist]
            # dist는 % 4로 안해주면 계속 커지므로 나머지로 접근
            dist = (dist + 1) % 4
            # 다시 출발
            r += di[dist]
            c += dj[dist]

    print(f'#{tc}')
    for j in arr:
        print(*j)






