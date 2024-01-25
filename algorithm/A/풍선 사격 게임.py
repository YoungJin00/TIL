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
    
    
    
# 2
T = int(input())

for tc in range(1, T + 1):

    N = int(input())

    balloon_lst = list(map(int, input().split()))

    max_score = 0

    def find_score(lst, score):
        # global 변수
        global max_score

        # 백트래킹
        tmp_total = 0
        tmp = len(lst) - 2
        if tmp > 0:
            tmp_total += (1000 ** 2) * tmp
            tmp_total += 2000
        else:
            tmp_total += len(lst) * 1000

        if score + tmp_total <= max_score:
            return

        # 종료조건
        if len(lst) == 0:
            max_score = max(score, max_score)
            return

        # 실행문
        if len(lst) == 1:
            tmp = lst.pop()
            find_score(lst, score + tmp)
            lst.append(tmp)

        else:
            for i in range(len(lst)):
                if i == 0:
                    tmp = lst.pop(0)
                    find_score(lst, score + lst[0])
                    lst.insert(0, tmp)
                elif i == len(lst) - 1:
                    tmp = lst.pop()
                    find_score(lst, score + lst[i - 1])
                    lst.append(tmp)
                else:
                    tmp = lst.pop(i)
                    find_score(lst, score + (lst[i - 1] * lst[i]))
                    lst.insert(i, tmp)

    find_score(balloon_lst, 0)

    print(f"#{tc} {max_score}")