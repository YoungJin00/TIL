# 가장빠른 문자열 타이핑

T = int(input())

for tc in range(1, T+1):
    A, B = input().split()
    C = len(A.replace(B, '0'))
    print(f'#{tc} {C}')


