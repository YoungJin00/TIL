# 전기버스 2

def dfs(idx, cnt):
    global MIN
    if idx >= N-1:
        MIN = min(MIN, cnt)
        return

    if cnt >= MIN:
        return

    for i in range(1,charges[idx]+1):
        dfs(idx+i, cnt+1)


T = int(input())

for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    N = lst[0]
    charges = lst[1:]
    MIN = float('inf')

    dfs(0, 0)

    print(f'#{tc} {MIN-1}')

# def bfs(idx, cnt):
#     global MIN
#
#     if idx >= N-1:
#         MIN = min(MIN, cnt)
#         return
#     if MIN < cnt:
#         return
#
#     for i in range(1, charges[idx]+1):
#         bfs(idx+i, cnt+1)
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     lst = list(map(int, input().split()))
#     N = lst[0]
#     charges = lst[1:]
#     MIN = float('inf')
#     bfs(0, 0)
#
#     print(f'#{tc} {MIN-1}')