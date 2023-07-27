# 소인수 분해

n = int(input())

if n == 1:
    print('')

for i in range(2, n +1):
    if n % i == 0:
        # 해당 숫자로 나눌 수 없을 때까지 나누기
        while n % i == 0:
            print(i)
            n = n / i




