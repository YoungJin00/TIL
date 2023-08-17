# 피자 굽기
t = int(input())

for tc in range(1, t + 1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))

    pizza = [(i + 1, C[i]) for i in range(M)]
    inpi = pizza[:N]
    pizza = pizza[N:]

    while len(inpi) != 1:
        idx, c = inpi.pop(0)
        c //= 2
        if c: inpi.append((idx, c))
        else:
            if pizza: inpi.append(pizza.pop(0))
    print(f'#{tc} {inpi.pop()[0]}')