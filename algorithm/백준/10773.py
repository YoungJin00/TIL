# 제로
N = int(input())

num_lst = []
for i in range(N):
    n = int(input())
    if n != 0:
        num_lst.append(n)
    else:
        num_lst.pop()

print(sum(num_lst))