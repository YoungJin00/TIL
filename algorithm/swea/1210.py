for tc in range(1, 11):
    _ = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    
    for i in range(100):
        if ladder[99][i] == 2:
            # 출발열 할당
            col = i
            break
    # 출발 행 할당
    row = 99
    
    while row > 0:
        
        # 위로 가기
        row -= 1
        
        # 왼쪽으로 이동
        if col > 0 and ladder[row][col-1] ==1:
            while col < 0 and ladder[row][col-1] == 1:
                col -= 1
        # 오른쪽으로 이동
        if col < 99 and ladder[row][col+1] == 1:
            while col < 99 and ladder[row][col+1] == 1:
                col += 1
        
    print(f'#{tc} {col}')
    





# direction 설정 (위, 오, 왼)
# dr = [-1, 0, 0]
# dc = [0, 1, -1]
#
# T = 10
# for tc in range(1, T+1):
#     t = int(input())
#     # 양 끝에 벽을 세워주기 위해 0 컬럼 추가
#     a = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
#
#     # c: 도착점 column idx 구하기
#     for j in range(102):
#         if a[99][j] == 2:
#             c = j
#
#     # 방향 위로 초기화
#     d = 0  # 0: 위, 1: 오, 2: 왼
#     r = 99
#     while True:
#         # 반복문 계속 돌리다가 row 인덱스가 0 이 되면 끝내고 리턴
#         if r == 0:
#             break
#
#         # 왼쪽에 1이 있으면 왼쪽으로 계속 가다가 0 나오면 반복문 종료
#         if a[r][c-1]:
#             d = 2
#             while True:
#                 r += dr[d]
#                 c += dc[d]
#                 if a[r][c-1] == 0:
#                     break
#
#         # 오른쪽에 1이 있으면 오른쪽으로 계속 가다가 0 나오면 반복문 종료
#         elif a[r][c+1]:
#             d = 1
#             while True:
#                 r += dr[d]
#                 c += dc[d]
#                 if a[r][c+1] == 0:
#                     break
#
#         # 양옆에 1 하나도 없으면 계속 직진(i.e. d=0) 또는
#         # 왼쪽이든 오른쪽이든 가다가 next col에서 0이면 d=0(위)로 체인지
#         d = 0
#         r += dr[d]
#         c += dc[d]
#
#     print("#{} {}".format(t, c-1))