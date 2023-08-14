# 문자열의 거울상

for tc in range(1, int(input())+1):
    words = input()[::-1]
    res = ''
    for i in words:
        if i == 'b':
            res += 'd'
        elif i == 'd':
            res += 'b'
        elif i == 'p':
            res += 'q'
        else:
            res += 'p'


    print(f'#{tc} {res}')

