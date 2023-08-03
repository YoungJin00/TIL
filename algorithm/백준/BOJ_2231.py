# 분해합

# 자연수 N
# 분해합은 각 자리수의 합 ex) 245 > 245 + 2+4+5 > 256

N = int(input())

for i in range(1, N+1):
    num = sum(map(int, str(i)))
    sum_num = i + num
    if sum_num == N:
        print(i)
        break
    if i == N:
        print(0)




