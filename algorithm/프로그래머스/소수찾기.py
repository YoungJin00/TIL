from itertools import permutations

# 소수 판단
def is_Prime(n):
    if n < 2:
        return False
    # 제곱근 활용하여 그 정수 만큼만 판단해도 소수 판단 가능
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    result = set()

    for i in range(1, len(numbers) + 1):
        # 순열 만들어 진게 자리 수 만큼 만들어줌
        perms = permutations(numbers, i)
        for perm in perms:
            num = int(''.join(perm))
            if is_Prime(num):
                # set 에 넣어주면서 중복 제거
                result.add(num)

    answer = len(list(result))
    return answer