# 동철이의 일 분배

def bfs(visited, idx, total_value):
    global MAX
    if idx == N:
        MAX = max(MAX, total_value)
        return

    if total_value <= MAX:
        return

    for i in range(N):
        if not used[i]:
            used[i] = True
            new_value = total_value * work[idx][i] / 100
            bfs(visited, idx + 1, new_value)
            used[i] = False


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    work = [list(map(int, input().split())) for _ in range(N)]
    used = [False] * N
    MAX = 0
    bfs(used, 0, 1) # 초기 가치는 100%
    MAX *= 100  # 백분율로 변환
    print(f'#{tc} {MAX:.6f}')