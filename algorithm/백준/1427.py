# 소트인사이드
import sys

input = sys.stdin.readline

N = input()

lst = list(N)
lst.sort(reverse=True)
res =''.join(lst)
print(res)