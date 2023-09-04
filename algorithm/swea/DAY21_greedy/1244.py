# 최대 상금
# 다양한 풀이가 존재할 수 있음
# 문제해석이 쉬운편

T = int(input())

for tc in range(1, T+1):
    numbers, cnt = input().split()
    cnt = int(cnt)
    nums = set([numbers])
    SET = set()

    for _ in range(cnt):
        while nums:
            n = nums.pop()
            n = list(n)
            for i in range(len(numbers)):
                for j in range(i+1, len(numbers)):
                    n[i], n[j] = n[j], n[i]
                    SET.add(''.join(n))
                    n[i], n[j] = n[j], n[i]
        nums, SET = SET, nums

    res = max(nums)
    print(f'#{tc} {res}')