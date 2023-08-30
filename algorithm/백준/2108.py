# 통계학
import sys
input = sys.stdin.readline

'''
산술평균
중앙값
최빈값 
범위 : 최대 최소 차이
'''
N = int(input())
lst = []
for i in range(N):
    num = int(input())
    lst.append(num)

# 산술
mean = round(sum(lst) / N)

# 중앙
sort_lst = sorted(lst)
mid = sort_lst[N//2]

# 최빈
from collections import Counter

cnt = Counter(lst)
mode = sorted(cnt.keys(), key=lambda a: (-cnt[a], a)) # - 붙히는 이유 내림차순 정렬
MAX = cnt[mode[0]]

modes = [num for num in mode if cnt[num] == MAX]
modes.sort()
if len(modes) > 1:
    mode = modes[1]
else:
    mode = modes[0]


# 범위
ran = max(lst) - min(lst)

print(mean)
print(mid)
print(mode)
print(ran)


