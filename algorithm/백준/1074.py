# N, r, c
# r행 c열 몇번쨰 방문
# 2 ** (N-1) x 2 ** (N-1)
import sys
input = sys.stdin.readline
def f(n, r, c):
    global res
    if n == 2:
        if r == R and c == C:
            print(res)
            return
        res += 1
        if r == R and c+1 == C:
            print(res)
            return
        res += 1
        if r+1 == R and c == C:
            print(res)
            return
        res += 1
        if r+1 == R and c+1 == C:
            print(res)
            return
        res += 1
        return
    f(n/2, r, c)
    f(n/2, r, c+n/2)
    f(n/2, r+n/2, c)
    f(n/2, r+n/2, c+n/2)


res = 0
N, R, C = map(int, input().split())
f(2**N, 0, 0)


def calculate_visit_order(N, R, C):
    if N == 0:
        return 0
    size = 2 ** (N - 1)
    quad_size = size * size
    quad_index = 0

    if R >= size:
        quad_index += 2
        R -= size
    if C >= size:
        quad_index += 1
        C -= size

    return quad_size * quad_index + calculate_visit_order(N - 1, R, C)

N, R, C = map(int, input().split())
print(calculate_visit_order(N, R, C))
