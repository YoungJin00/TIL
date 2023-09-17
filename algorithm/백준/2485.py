from math import gcd
import sys
input = sys.stdin.readline

# 이미 심은 가로수 수
N = int(input())

# 첫 가로수 위치
a = int(input())

#가로수들 사이 값 저장할 리스트
lst = []
for _ in range(N-1):
    num = int(input())
    lst.append(num - a)
    a = num

# lst에 들어있는 모든 수들의 최대공약수 찾기
g = lst[0]
for i in range(1, len(lst)):
    g = gcd(g, lst[i])

res = 0
for each in lst:
    res += each // g -1

print(res)



