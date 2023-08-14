# 문자열 비교

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    cnt = 0
    if str1 in str2:
        cnt += 1

    print(f'#{tc} {cnt}')