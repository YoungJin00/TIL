# 트로피 진열
def f(lst):
    now = lst[0]
    cnt = 1
    for i in range(1, len(lst)):
        if now < lst[i]:
            cnt += 1
            now = lst[i]
    return cnt

N = int(input())
lst = [int(input()) for _ in range(N)]

print(f(lst))
lst.reverse()
print(f(lst))