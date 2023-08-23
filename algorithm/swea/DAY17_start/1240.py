
T = int(input())

dic = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5,
       '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

for tc in range(1, T+1):
    N, M = map(int, input().split())
    MAP = [input() for _ in range(N)]

    row_code = ''
    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if MAP[i][j] == '1':
                row_code += MAP[i]
                break
        if row_code:
            break

    code = row_code[::-1]

    for i in range(len(code)):
        if code[i] == '1':
            code = code[i:i+56]
            break

    code = code[::-1]

    lst = []
    for i in range(0, 56, 7):
        lst.append(code[i:i+7])

    num = []
    for i in lst:
        num.append(dic[i])
    # lst, num 줄이기
    # num = [dic[code[i:i + 7]] for i in range(0, 56, 7)]

    a = b = 0
    for i in range(0, 8, 2):
        a += num[i]
        b += num[i+1]

    res = 0
    for i in range(8):
        if (a * 3 + b) % 10 == 0:
            res += num[i]
        else:
            res = 0
    print(f'#{tc} {res}')