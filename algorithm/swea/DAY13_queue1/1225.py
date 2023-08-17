# 암호 생성기
for _ in range(10):
    tc = int(input())
    password = list(map(int, input().split()))

    cnt = 0
    while True:
        cnt = (cnt % 5) + 1
        if password[0] != 0:
            m = password.pop(0) - cnt
            if m < 0 :
                m = 0
            password.append(m)
        if password[-1] == 0:
            break
    print(f'#{tc}', *password)