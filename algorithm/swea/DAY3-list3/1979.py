T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    # print(puzzle)

    # 가로 확인
    word = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
            # 현재 위치에 있는 요소가 0이거나 현재 열이 행의 끝(N-1)에 도달한 경우
            if puzzle[i][j] == 0 or j == N-1:
                if cnt == K:
                    word += 1
                if puzzle[i][j] == 0:
                    cnt = 0
    # 세로 확인
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[j][i] == 1:
                cnt += 1
            if puzzle[j][i] == 0 or j == N-1:
                if cnt == K:
                    word += 1
                if puzzle[j][i] == 0:
                    cnt = 0
    print(f'#{tc} {word}')




    # print(cnt, word)


