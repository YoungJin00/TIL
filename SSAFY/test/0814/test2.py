# 괄호연산
# for tc in range(1, int(input()) + 1):
#     # 배열에 들아갈 수식이 공백없이 받아오기
#     words = input()
#     stack = []
#     SUM = 0
#
#     for i in range(len(words)):
#         # words의 인덱스 값이 '(', '{' 이면 스택에 값추가
#         if words[i] == '(' or words[i] == '{':
#             stack.append(words[i])
#
#         # 인덱스값이 ')' 값일때
#         elif words[i] == ')':
#             # 스택에 값이 있고 스택 마지막값이 ( 일경우 스택에서 제거 아니라면 인덱스값 추가
#             if stack and stack[-1] == '(':
#                 stack.pop()
#             else:
#                 stack.append(words[i])
#         # 인덱스값이 '}' 값일때
#         elif words[i] == '}':
#             # 스택에 값이 있고 스택 마지막값이 { 일경우 스택에서 제거 아니라면 인덱스값 추가
#             if stack and stack[-1] == '{':
#                 stack.pop()
#             else:
#                 stack.append(words[i])
#     # print(stack)
#
#     if stack:
#         print(f'#{tc} -1')
#     else:
#         print(f'#{tc} 1')


T = int(input())
# 괄호 검사
def check(words): # 괄호검사
    stack = [0] * 100
    sp = -1

    for w in words:
        if w in ['(', '{']: # 여는 괄호 push
            sp += 1
            stack[sp] = w
        elif w == ')':
            if sp >= 0 and stack[sp] == '(':
                sp -= 1
            else:
                return 0
        elif w == '}':
            if sp >= 0 and stack[sp] == '{':
                sp -= 1
            else:
                return 0
    if sp >= 0:
        return 0

    else:
        return 1

# 괄호 정상인 수식들만
def calculate(words):
    stack = [0] * 100
    sp = -1

    for w in words:
        if w not in [')', '}']: # 숫자나, 여는 괄호 push
            sp += 1
            stack[sp] = w
        elif w == ')':
            temp = 0
            while sp > -1 and stack[sp] != '(':
                temp += int(stack[sp])
                sp -= 1 # pop 하기
            sp -= 1 # '(' pop
            sp += 1
            stack[sp] = temp # 연산결과 푸쉬
        elif w == '}':
            temp = 1
            while sp > -1 and stack[sp] != '{':
                temp *= int(stack[sp])
                sp -= 1 # pop 하기
            sp -= 1 # '(' pop
            sp += 1
            stack[sp] = temp # 연산결과 푸쉬

    if sp != 0:
        return -1
    else:
        return stack[sp]




for t in range(1, T+1):
    words = input()
    ans = -1

    if check(words):
        ans = calculate(words)

    print(f'#{t} {ans}')


