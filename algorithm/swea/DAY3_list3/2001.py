# 파리 퇴치
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    fly_map = [list(map(int, input().split())) for _ in range(N)]

    sum_fly = []

    for i in range(N-M+1):
        for j in range(N-M+1):
            fly = 0
            for k in range(M):
                for l in range(M):
                    fly += fly_map[i+k][j+l]
                sum_fly.append(fly)

        max_fly = max(sum_fly)
    print(f'#{tc} {max_fly}')



# T = int(input())

# for t in range(1, T+1):
#     N, M = map(int,input().split())

#     lst = [list(map(int,input().split())) for _ in range(N)]

#     MAX = 0

#     for i in range(N):
#         for j in range(N):
#             SUM = 0

#             for x in range(M):
#                 for y in range(M):
#                     if 0 <= i + x < N and 0 <= j + y < N:
#                         SUM += lst[i + x][j + y]
#             if MAX < SUM:
#                 MAX = SUM

#     print(f'#{t} {MAX}')
