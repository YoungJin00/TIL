T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    answer = list(map(int, input().split()))

    MAX = 0
    MIN = 987654321
    for _ in range(N):
        student = list(map(int, input().split()))
        score = 0
        cnt = 0

        for i in range(M):
            if student[i] == answer[i]:
                score += 1 + cnt
                cnt += 1
            else:
                cnt = 0
        if MAX < score:
            MAX = score
        if MIN > score:
            MIN = score

        result = MAX - MIN
    print(f'#{tc} {result}')

