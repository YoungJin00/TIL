T = int(input())
for tc in range(1, T + 1):
    MAP = [list(map(int, input().split())) for _ in range(9)] # 2차원 배열 입력
    rowMAP = MAP #가로 배열은 입력받은 배열과 동일
    colMAP = []
    # 세로행
    for i in range(9):
        col = []
        for j in range(9):
            col.append(MAP[j][i])
        colMAP.append(col)

    # 3 X 3
    sqrMAP = []
    for i in range(3):
        for j in range(3):
            square = []
            for k in range(3):
                for l in range(3):
                    row = i * 3 + k
                    col = j * 3 + l
                    square.append(MAP[row][col])
            sqrMAP.append(square)
    # sqrMAP = []
    # for i in range(9):
    #     square = []
    #     for j in range(9):
    #         row = i % 3 * 3 + j // 3
    #         col = i // 3 * 3 + j % 3
    #         square.append(MAP[row][col])
    #     sqrMAP.append(square)

    ans = 1 #출력할 정답
    for row, col, sqr in zip(rowMAP, colMAP, sqrMAP): # 2차원배열에서 각각 1차원 배열을 꺼내서
        if len(set(row)) == len(set(col)) == len(set(sqr)) == 9: # 집합으로 변환했을때 길이가 모두 9이면
            continue # 통과
        else: #아니면 (스도쿠 조건 충족 X)
            ans = 0 #정답 0으로 설정
            break # 반복 중단
    print(f'#{tc} {ans}')

    # colMAP = [[MAP[i][j] for i in range(9)] for j in range(9)] #새로 배열 변환
    # sqrMAP = [[MAP[i % 3 * 3 + j // 3][i // 3 * 3 + j % 3] for j in range(9)] for i in range(9)] # 3 * 3 사각형 각각을 1차원 배열로 변환

    sqrMAP = []
    for i in range(3):
        for j in range(3):
            square = []
            for k in range(3):
                for l in range(3):
                    row = i * 3 + k
                    col = j * 3 + l
                    square.append(MAP[row][col])
            sqrMAP.append(square)


