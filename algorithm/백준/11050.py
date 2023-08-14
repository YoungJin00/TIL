# 이항 계수

N, K = map(int, input().split())
total1 = 1
total2 = 1
for i in range(N, N-K, -1):
    total1 *= i

for i in range(K, 0, -1):
    total2 *= i

print(total1//total2)

