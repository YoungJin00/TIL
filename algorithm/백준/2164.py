# 카드 2
from collections import deque

N = int(input())

li = deque()

for i in range(1, N + 1):
    li.append(i)

while len(li) > 1:
    li.popleft()  # 첫 번째 수 제거
    li.append(li.popleft())  # 첫 번째 수를 맨 뒤로 이동

print(li[0])