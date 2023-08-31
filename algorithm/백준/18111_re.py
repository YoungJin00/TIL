# 마인크래프트
import sys
N, M, B = map(int, input().split())

heights = []  # 각 땅의 높이 정보 저장

for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    heights.extend(row)

min_height = min(heights)
max_height = max(heights)
min_time = float('inf')  # 최소 시간 초기화
best_height = 0          # 최적 높이

for target in range(min_height, max_height+1):
    b_above = 0
    b_below = 0

    for h in heights:
        if h > target:
            b_above += ( h - target)
        else:
            b_below += (target - h)

    required_block = b_below + b_above

    if required_block <= B:  # 인벤토리에 충분한 블록이 있는 경우
        time = b_above * 2 + b_below
        if min_time >= time:
            min_time = time
            best_height = target

print(min_time, best_height)