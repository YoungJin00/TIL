#
T = int(input())

for tc in range(1, T+1):
    a = int(input())
    b = int(input())
    li = [x for x in range(1, b+1)]
    for i in range(a):
        for j in range(1, b):
            li[j] += li[j - 1]
    print(li[-1])


