# 팩토리얼 0의 개수
import sys

N = int(sys.stdin.readline())

cnt = 0
while N >= 5:
    cnt += N // 5
    N //= 5

print(cnt)