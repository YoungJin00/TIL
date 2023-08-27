T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = []
    for _ in range(N):
        words = input()
        lst.append(words[0])
    lst.sort()
    cnt = 1
    for i in range(1, len(lst)):
        if lst[0] == 'A':
            if ord(lst[i]) == ord(lst[i-1]):
                continue
            elif ord(lst[i]) == ord(lst[i-1]) + 1:
                cnt += 1
            else:
                break
        else:
            cnt = 0
            break
    print(f'#{tc} {cnt}')