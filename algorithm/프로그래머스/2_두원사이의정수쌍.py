r1 = 2
r2 = 3
cnt = 0
for x in range(-r2, r2 + 1):
    for y in range(-r2, r2 + 1):
        if x ** 2 + y ** 2 <= r2 ** 2 and x ** 2 + y ** 2 >= r1 ** 2:
            cnt += 1


print(cnt)

import math


def solution(r1, r2):
    answer = 0

    for i in range(1, r2 + 1):
        high_r1 = math.sqrt(r2 ** 2 - i ** 2)
        high_r2 = 0 if i > r1 else math.sqrt(r1 ** 2 - i ** 2)

        answer += math.floor(high_r1) - math.ceil(high_r2) + 1

    return answer * 4


