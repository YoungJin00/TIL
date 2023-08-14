# 괄호검사

def is_valid(words):
    stack = []
    mapping = {')' : '(', ']' : '[', '}' : '{'}
    for w in words:
        if w in mapping.values():
            stack.append(w)
        elif w in mapping.keys():
            if stack and stack[-1] == mapping[w]:
                stack.pop()
            else:
                return False
        else:
            continue

    return not stack # stack이 비어있으면 True, False

for tc in range(1, int(input())+1):
    words = input()
    a = int(is_valid(words))
    print(f'#{tc} {a}')


# def is_valid(words):
#     stack = []
#     mapping = {')': '(', ']': '[', '}': '{'}
#
#     for w in words:
#         if w in mapping.values():
#             stack.append(w)
#         elif w in mapping.keys() and (not stack or stack.pop() != mapping[w]):
#             return False
#
#     return not stack
#
#
# for tc in range(1, int(input()) + 1):
#     words = input()
#     a = int(is_valid(words))
#     print(f'#{tc} {a}')