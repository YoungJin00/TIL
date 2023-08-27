T = int(input())
for tc in range(1, T+1):
    words = input()

    leng = 0

    for i in range(1, 11):
        if words[:i] == words[i:i*2]:
            leng = i
            break
    print(f'#{tc} {leng}')






