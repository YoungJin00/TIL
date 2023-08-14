'''
(6+5*(2-8)/2)
'''

stack = [0] * 100
top = -1
icp = {'(':3, '*':2, '/':2, '+':1, '-':1}
isp = {'(':0, '*':2, '/':2, '+':1, '-':1}

fx = '(6+5*(2-8)/2)'
sik = ''
for x in fx:
    if x not in '(+-*/)':
        sik += x
    elif x == ')':
        while stack[top] != '(':
            sik += stack[top]
            top -= 1
        top -= 1 # '(' 버림.

    else:
        if top == -1 or isp[stack[top]] < icp[x]: # 토큰의 우선순위가 더 높으면
            top += 1
            stack[top] = x
        elif isp[stack[top]] >= icp[x]:
            while top > -1 and isp[stack[top]] >= icp[x]:
                sik += stack[top]
                top -= 1
            top += 1
            stack[top] = x
print(sik)

for x in sik:
    if x not in '+-/*':   # 피연산자면...
        top += 1
        stack[top] = int(x)
    else:
        op1 = stack[top]  # pop()
        top -= 1
        op2 = stack[top]  # pop()
        top -= 1
        if x == '+': # op2 + op1
            top += 1  # 2줄 합쳐서 push 동작
            stack[top] = op2 + op1

        elif x == '-':
            top += 1
            stack[top] = op2 - op1

        elif x == '/':
            top += 1
            stack[top] = op2 // op1

        elif x == '*':
            top += 1
            stack[top] = op2 * op1

print(stack[top])