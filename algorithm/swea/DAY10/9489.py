# 고대유적

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    MAP = [list(map(int, input().split())) for _ in range(N)]
    # print(MAP)
    cnt = 0
    res = 0

    for i in range(N):
        for j in range(M):
           if MAP[i][j] == 1:
               cnt += 1
               if MAP[i][j] == 0:
                   cnt = 0

    print(f'#{tc} {cnt}')

'''
3
3 3
0 1 0
0 1 0
0 1 0
3 3
0 1 0
1 1 1
0 0 0
8 8
1 0 0 0 0 0 1 0
1 0 1 1 1 0 1 0
1 0 0 0 0 0 1 0
0 0 0 1 0 0 1 0
0 0 0 1 0 0 1 0
0 1 1 0 0 0 1 0
0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1
'''