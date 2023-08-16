# 수열 ,,쉽지만 시간초과,, 쉬운게 아님
# import sys
#
# N, K = map(int, sys.stdin.readline().split())
#
# lst = list(map(int, sys.stdin.readline().split()))
#
# total = 0
# MAX = 0
# for i in range(N-K+1):
#     total = lst[i:i+K]
#
#     if MAX < total:
#         MAX = total
# print(MAX)
'''
10 5
3 -2 -4 -9 0 3 7 13 8 -3
-12 -12 -3 14 31 28 0
'''
import sys

N, K = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

# 처음에 total K만큼 값 더해서 할당
total = sum(lst[:K])
# 최대값에 처음 total값 할당
MAX = total


for i in range(N - K):
    # total에 lst의 첫번째 값 빼주고 마지막값 더해주고
    total = total - lst[i] + lst[i + K]
    # MAX에 MAX, total 중에 맥스값 출력
    MAX = max(MAX, total)

print(MAX)