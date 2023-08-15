# 미로찾기
def DFS(x, y):
    if MAP[x][y] == '3':  # 현재 위치가 목표 지점('3')이면 1 반환
        return 1

    MAP[x][y] = '1'  # 현재 위치를 방문한 것으로 표시 ('1')
    for i in range(4):  # 상하좌우로 이동하는 4가지 방향에 대해 반복
        ni, nj = x + di[i], y + dj[i]  # 다음 위치 계산
        if 0 <= ni < N and 0 <= nj < N and MAP[ni][nj] != '1':  # 다음 위치가 유효하고, 아직 방문하지 않았으면
            if DFS(ni, nj):  # 다음 위치에서 DFS를 재귀 호출하여 도달 가능한지 확인
                return 1  # 도달 가능하면 1 반환
    return 0  # 모든 방향으로 도달 불가능하면 0 반환

di = [0, 1, 0, -1]  # 상하좌우 이동을 나타내는 배열
dj = [1, 0, -1, 0]
for tc in range(1, int(input()) + 1):  # 테스트 케이스 수 만큼 반복
    N = int(input())  # 맵의 크기 N 입력
    MAP = [list(input()) for _ in range(N)]  # N x N 크기의 맵 정보 입력

    for i in range(N):
        for j in range(N):
            if MAP[i][j] == '2':  # 출발 지점('2')을 찾으면
                res = DFS(i, j)  # DFS를 시작하여 도달 가능한지 판단

    print(f'#{tc} {res}')  # 결과 출력