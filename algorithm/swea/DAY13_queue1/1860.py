'''
N : 자격 얻은 사람
M초동안  K개 붕어빵

#진기의 최고급 붕어빵
'''
t = int(input())

for tc in range(1, t+1):
    N, M, K = map(int, input().split())
    # 오름차순으로 정렬
    arrive = sorted(map(int, input().split()))
    res = 'Possible'
    
    for i in range(N):
        # 도착시간에 붕어빵 만들어진 개수가 음수이면
        if (arrive[i] // M) * K - (i+1) < 0:
            res = 'Impossible'
            break

    print(f'#{tc} {res}')



