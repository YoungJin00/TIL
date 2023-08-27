# T = int(input())
#
# for tc in range(1, T+1):
#     n = int(input())
#
#     MAP = [list(map(int, input().split())) for _ in range(n)]
#
#     lst = []
#     cnt = 0
#     for i in range(n):
#         for j in range(n):
#             if MAP[i][j] != 0:
#                 y, x = i, j
#                 while y < n and MAP[y][j] != 0:
#                     y += 1
#                 while x < n and MAP[i][x] != 0:
#                     x += 1
#
#                 lst.append((y-i, x-j))
#
#                 for k in range(i, y):
#                     for l in range(j, x):
#                         MAP[k][l] = 0
#
#     lst.sort(key=lambda a: (a[0] * a[1], a[0]))
#
#     print(f"#{tc} {len(lst)}", end=' ')
#     for y, x in lst:
#         print(f"{y} {x}", end=" ")
#     print()

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    lst = []

    for i in range(N):
        for j in range(N):
            if MAP[i][j] != 0: # 0이 아닐때 좌표 구해주기
                y, x = i, j

                while y < N and MAP[y][j] != 0: # 행이 N범위안벗어나고  0이 아닐때
                    y += 1                      # y 값 1씩 더함

                while x < N and MAP[i][x] != 0: # 열이 N 범위 안벗어나고 0 이 아닐때
                    x += 1                      # x 값 1씩 더함

                lst.append((y-i, x-j))          # 리스트에 추가 해주기

                for k in range(i, y):           # i 부터 y 전까지 지나간곳 0으로 체크
                    for l in range(j, x):       # j 부터 x 전까지 지나간곳 0으로 체크
                        MAP[k][l] = 0

    lst.sort(key=lambda a: (a[0] * a[1], a[0])) # lst 속성 a로 불러와서 a[0]*a[1], a[0]
                                                # 크기가 같을때 a[0] 원소

    print(f"#{tc} {len(lst)}", end=' ')
    for y, x in lst:
        print(f"{y} {x}", end=" ")
    print()













