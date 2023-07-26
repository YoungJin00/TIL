# 소수 찾기

n = int(input())
numbers = list(map(int, input().split()))

cnt = 0

for num in numbers:
    if num < 2:
        continue
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        cnt += 1

print(cnt)
        
    