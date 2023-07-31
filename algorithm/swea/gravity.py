# 

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))
    max1 = 0
    
    for i in range(N):
        cnt = 0
        # i번째 원소 이후의 원소들과만 비교
        for j in range(i+1, N):
            if li[i] > li[j]:
                cnt += 1
        if cnt > max1:
            max1 = cnt
    print(f'#{tc} {max1}')
