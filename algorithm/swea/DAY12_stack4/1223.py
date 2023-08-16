# 계산기 2
'''
계산식을 후위 표기식으로 바꾸어 계산하는 프로그램 작성
“3+4+5*6+7”  >> "34+56*+7+"

'''


for tc in range(1, 11):
    N = int(input())
    sik = input()
    stack = []
    icp = {'*': 2, '+': 1}
    isp = {'*': 2, '+': 1}
    cal = ''

    for x in sik:
        if x not in '+*':
            cal += x
        else:
            while stack and isp[stack[-1]] >= icp[x]:
                cal += stack.pop()
            stack.append(x)
    while stack:
        cal += stack.pop()

    for x in cal:
        if x not in '+*':
            stack.append(int(x))
        else:
            op1 = stack.pop()
            op2 = stack.pop()

            if x == '+':
                stack.append(op2 + op1)
            else:
                stack.append(op2 * op1)

    print(f'#{tc} {stack[0]}')