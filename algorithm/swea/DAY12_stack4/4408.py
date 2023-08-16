# 자기방으로 돌아가기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 400개 방만큼 여유공간 만들어 두기
    stack = [0] * 401
    room_lst = []
    for _ in range(N):
        room = list(map(int, input().split()))
        room_lst.append(room)
    # print(room_lst)
    for room in room_lst:
        # print(room)
        # 출발, 도착 지정
        '''
        처음 400으로 했을땐 끝이 홀수이면 +1에도 영향 앞이 짝수면 -1 방에도 영향을 미침
        [1,3][4,6] 3,4가 복도에서 만나서 최종값이 2가 된다
        '''
        if room[0] < room[1]:
            s = (room[0] + 1) // 2
            e = (room[1] + 1) // 2
        else:
            e = (room[0] + 1) // 2
            s = (room[1] + 1) // 2
        # 지나간 공간에 1로 채워주기
        for i in range(s, e+1):
            stack[i] += 1
    ans = max(stack)
    # print(stack)
    print(f'#{tc} {ans}')

'''
처음 400으로 했을땐 끝이 홀수이면 +1에도 영향 앞이 짝수면 -1 방에도 영향을 미침
[1,3][4,6] 3,4가 복도에서 만나서 최종값이 2가 된다
'''
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     # 400개 방만큼 여유공간 만들어 두기
#     stack = [0] * 400
#     room_lst = []
#     for _ in range(N):
#         room = list(map(int, input().split()))
#         room_lst.append(room)
#     # print(room_lst)
#     for room in room_lst:
#         # print(room)
#         # 출발, 도착 지정
#         if room[0] < room[1]:
#             s = room[0]
#             e = room[1]
#         else:
#             e = room[0]
#             s = room[1]
#         # 지나간 공간에 1로 채워주기
#         for i in range(s, e+1):
#             stack[i] += 1
#     ans = max(stack)
#     # print(stack)
#     print(f'#{tc} {ans}')