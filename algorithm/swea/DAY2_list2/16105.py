# 숫자 카드
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = input()
    li = [0] * 12
    max_idx = 0
    for i in num:
        i = int(i)
        li[i] += 1
        max_idx = i
    res = max(li)



    print(f'#{tc} {max_idx} {res}')
