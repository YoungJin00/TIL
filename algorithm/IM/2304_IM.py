N = int(input())

MAX = 0
idx = 0
lst = [0] * 1001
for _ in range(N):
    L, H = map(int, input().split()) # L 왼쪽면, H 높이
    lst[L] = H
    if MAX < H:
        MAX = H
        idx = L

height = 0
res = 0
# 순회하면서 max값을 바꿔주면서 더해줌
for i in range(idx+1): # 맥스값 왼쪽부분
    height = max(height, lst[i])
    res += height

height = 0
for i in range(1000, idx, -1): # 맥스값 오른쪽 부분
    height = max(height, lst[i])
    res += height

print(res)


