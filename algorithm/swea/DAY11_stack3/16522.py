# forth
for tc in range(1, int(input()) + 1):
    stack = []
    words = input().split()
    for w in words:
        if w not in '+-*/.':
            stack.append(int(w))
        elif w == '.':
            if len(stack) == 1:
                res = stack.pop()
            else:
                res = 'error'
        else:
            if len(stack) > 1:
                a = stack.pop()
                b = stack.pop()
                if w == '+':
                    stack.append(b + a)
                elif w == '-':
                    stack.append(b - a)
                elif w == '*':
                    stack.append(b * a)
                elif w == '/':
                    stack.append(b // a)
            else:
                res = 'error'
                break

    print(f'#{tc} {res}')