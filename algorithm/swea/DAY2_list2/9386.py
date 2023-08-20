# 연속한 1의 개수

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    li = input()
    cnt = 0
    res = 0
    for i in li:
        i = int(i)
        if i == 0:
            cnt = 0
        else:
            cnt += 1
            if res < cnt:
                res = cnt

    print(f'{tc} {res}')

