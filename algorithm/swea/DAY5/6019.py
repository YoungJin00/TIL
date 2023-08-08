# 기차 사이의 파리

T = int(input())

for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())

    pari = D / (A+B)
    pari_idong = F * pari
    sosu = format(pari_idong, '.6f')

    print(f'#{tc} {sosu}')