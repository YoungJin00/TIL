# 반복문자 지우기

T = int(input())

for tc in range(1, T+1):
    words = input()
    leng = len(words)
    stack = []
    top = -1
    for w in words:
        if stack:
            if w == stack[top]:
                stack.pop()
            else:
                stack.append(w)
        else:
            stack.append(w)

    res = len(stack)
    print(f'#{tc} {res}')