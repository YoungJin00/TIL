def calScore(lst):
    n = len(lst)

    if n == 3:
        return max(lst[1] * 3, lst[0] * lst[2] + max(lst[0], lst[2]) * 2)

    if tuple(lst) in memo:
        return memo[tuple(lst)]

    MAX = 0
    for i in range(n):
        if 0 < i < n -1:
            score = lst[i-1] * lst[i+1]
        elif i == 0:
            score = lst[0]
        else:
            score = lst[n-1]

        temp = lst.pop(i)
        score += calScore(lst)
        lst.insert(i, temp)

        if MAX < score:
            MAX = score

    memo[tuple(lst)] = MAX
    return MAX


T = int(input())
for t in range(1, T+1):
    N = int(input())
    balloons = list(map(int, input().split()))

    if len(balloons) == 2:
        result = max(balloons) * 2
    else:
        memo = {}
        result = calScore(balloons)

    print(f'#{t} {result}')