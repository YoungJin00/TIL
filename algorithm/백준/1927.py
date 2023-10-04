import heapq
import sys

input = sys.stdin.readline

N = int(input())

res = []
for i in range(N):
    command = int(input())
    if command == 0:
        if res:
            n = heapq.heappop(res)
            print(n)
        else:
            print(0)
    else:
        heapq.heappush(res, command)

