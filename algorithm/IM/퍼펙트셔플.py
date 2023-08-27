# 3499
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    words = input().split()
    lst = []
    ban = N // 2
    for i in range(ban):
        lst.append(words[i])
        lst.append(words[i + ban + (N % 2)])

    if N % 2 != 0: # 홀수 일때 중앙에 값 추가
        lst.append(words[N // 2])

    print(f'#{tc}', *lst)
