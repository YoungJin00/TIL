T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
#     우 하 상 좌
d = ['<', '>', '^', 'v']
for tc in range(1, T+1):
    H, W = map(int, input().split()) # H: 맵 높이, W:길이

    MAP = [ input() for _ in range(H)]

    N = int(input())
    command = input()
    # 전차 위치
    for i in range(H):
        for j in range(W):
            if MAP[i][j] in d:
                x, y = i, j

    for i in range(N):
        pass


'''
문자	의미
.	평지(전차가 들어갈 수 있다.)
*	벽돌로 만들어진 벽
#	강철로 만들어진 벽
-	물(전차는 들어갈 수 없다.)
^	위쪽을 바라보는 전차(아래는 평지이다.)
v	아래쪽을 바라보는 전차(아래는 평지이다.)
<	왼쪽을 바라보는 전차(아래는 평지이다.)
>	오른쪽을 바라보는 전차(아래는 평지이다.)
'''
