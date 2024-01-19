## DFS
def solution(numbers, target):
    stack = [(0, 0, 0)] # (now , index, depth)
    cnt = 0

    while stack:
        now, idx, depth = stack.pop()

        if depth == len(numbers):
            if now== target:
                cnt += 1
        else:
            stack.append((now+ numbers[idx], idx + 1, depth + 1))
            stack.append((now- numbers[idx], idx + 1, depth + 1))

    return cnt

## BFS
from collections import deque

def solution(numbers, target):
    queue = deque([(0, 0, 0)]) # (now , index, depth)
    cnt = 0

    while queue:
        now, idx, depth = queue.popleft()

        if depth == len(numbers):
            if now== target:
                cnt += 1
        else:
            queue.append((now+ numbers[idx], idx + 1, depth + 1))
            queue.append((now- numbers[idx], idx + 1, depth + 1))

    return cnt