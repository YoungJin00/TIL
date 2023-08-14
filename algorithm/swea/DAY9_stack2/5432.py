# 쇠막대기 자르기

for tc in range(1, int(input()) + 1):
    pipe = input()

    stack = []
    res = 0
    cnt = 0

    for i in range(len(pipe)):
        if pipe[i] == '(':
            stack.append(pipe[i])
        else:
            if stack and pipe[i-1] == '(':
                stack.pop()
                res += len(stack)
            else:
                cnt += 1
                stack.pop()
    result = res + cnt
    print(f'#{tc} {result}')