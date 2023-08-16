# 계산기 1

for tc in range(1, 11):
    N = int(input())
    sik = input()
    cal = ''
    stack = []
    isp = {'+': 1}
    icp = {'+': 1}

    for x in sik:
        if x not in '+':
            cal += x

        else:
            while stack and isp[stack[-1]] >= icp[x]:
                cal += stack.pop()
            stack.append(x)
    while stack:
        cal += stack.pop()

    for x in cal:
        if x not in '+':
            stack.append(int(x))
        else:
            a = stack.pop()
            b = stack.pop()
            if x == '+':
                stack.append(b+a)
    print(f'#{tc} {stack[0]}')





'''
for tc in range(1, 11):
    N = int(input())
    sik = input()
    stack = []
    for i in sik:
        if i != '+':
            stack.append(int(i))

    SUM = 0
    for i in stack:
        SUM += i

    print(f'#{tc} {SUM}')
'''


