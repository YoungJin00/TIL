# 봉우리
# 방향 설정 (우, 하, 좌, 상)
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 테스트 케이스 받아오기
for tc in range(1, int(input()) + 1):
    # 지도의 가로 세로 크기 N 받아오기
    N = int(input())
    # N개의 줄에 걸쳐 공백으로 구분된 N개의 높이 h로 2차원 리스트 만들기
    MAP = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            # 봉우리 값 할당
            s = MAP[i][j]
            bong = 0
            for k in range(4):
                # 4방향으로 돌면서 s 값과 값 비교
                ni, nj = i + di[k], j + dj[k]
                # ni, nj 가 범위 안이면서 s값보다 작을때 bong 1 씩 더하기
                if 0 <= ni < N and 0 <= nj < N and MAP[ni][nj] < s:
                    bong += 1
            # i, j가 모서리인경우 2개만 맞으면 카운트 1더하기
            if (i == 0 and j == 0) or (i == 0 and j == N-1) \
                    or (i == N-1 and j == 0) or (i == N-1 and j == N-1):
                if bong >= 2:
                    cnt += 1
            # i 나 j과 끝값일 경우 3개만 맞으면 카운트 1더하기
            elif i == 0 or j == 0 \
                    or i == N-1 or j == N-1:
                if bong >= 3:
                    cnt += 1
            # 나머지는 4가 더해져야 1 더하기
            else:
                if bong >=4:
                    cnt += 1

    print(f'#{tc} {cnt}')

'''
T = int(input())

dr = [0,0,1,-1]
dc = [1,-1,0,0]

for t in range(1,T+1):
    N = int(input())
    MAP = [list(map(int,input().split())) for _ in range(N)]

    cnt = 0

    for r in range(N):
        for c in range(N):
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < N and 0 <= nc < N: #MAP을 벗어나지않게
                    if MAP[r][c] <= MAP[nr][nc]:
                        break
            else:
                cnt += 1

    print(f'#{t} {cnt}')
'''


