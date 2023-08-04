# 현주의 상자 바꾸기

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())

    li = [0] * N
    for i in range(1, Q+1):
        I, R = map(int, input().split())
        for j in range(I-1, R):
            li[j] = i


    print(f'#{tc}', *li)


