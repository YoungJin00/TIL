T = int(input())

for tc in range(1, T+1):
    lst = []
    for i in range(5):
        words = input()
        lst.append(words)

    res = ''
    for i in range(15):
        for j in range(5):
            try:
                res += lst[j][i]
            except:
                continue

    print(f'#{tc} {res}')




