# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     lst = [list(map(int, input().split())) for _ in range(N)]
#
#     max_cnt = 0
#     max_start = 0
#     for p in range(N):
#         for q in range(N):
#             i, j = p, q
#             cnt = 1
#             start = lst[i][j]
#
#             while True:
#                 for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
#                     ni, nj = i + di, j+dj
#                     if 0 <= ni < N and 0<=nj<N and lst[i][j]+1 == lst[ni][nj]:
#                         cnt += 1
#                         i, j = ni, nj
#                         break
#                 else:
#                     break
#
#             if max_cnt < cnt:
#                 max_cnt = cnt
#                 max_start = start
#             elif max_cnt == cnt and max_start > start:
#                 max_start = start
#     print(f'#{tc} {max_start} {max_cnt}')


# def bfs(i, j, N):
#     global rm
#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]
#     q = [(i, j)]
#     cnt = 0
#     while q:
#         i, j = q.pop(0)
#         cnt += 1
#         if v[i][j] != 0:
#             return cnt + v[i][j]-1
#
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#             if 0 <= ni < N and 0<=nj<N and rm[i][j]+1 == rm[ni][nj]:
#                 q.append((ni, nj))
#     return cnt


# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     rm = [list(map(int, input().split())) for i in range(N)]
#     v = [[0] * N for i in range(N)]
#
#     maxV = 0
#     minV = 100000000
#     for i in range(N):
#         for j in range(N):
#             if v[i][j] == 0:
#                 v[i][j] = bfs(i,j,N)
#                 if (maxV < v[i][j]):
#                     maxV = v[i][j]
#                     minV = rm[i][j]
#                 elif maxV == v[i][j]:
#                     if minV > rm[i][j]:
#                         minV = rm[i][j]
#     print(f'#{tc} {minV} {maxV}')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    ones = [0] * (N*N+1) # 연속으로 1이 커지는 경우를 표시할 배열
    for i in range(N):
        for j in range(N):
            for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
                ni, nj = i+di, j+dj
                if 0 <= ni <N and 0<=nj<N and lst[i][j]+1 == lst[ni][nj]:
                    ones[lst[i][j]] = 1

    max_cnt = 0
    max_start = 0
    c = 0
    for k in range(N*N, 0, -1):
        if ones[k]:
            c += 1
            if max_cnt < c:
                max_cnt = c
                max_start = k
            elif max_cnt == c:
                max_start = k
        else:  #ones[k] 가 0이면
            c = 0
    print(f'#{tc} {max_start} {max_cnt+1}')






