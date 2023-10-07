# 대표값 2
lst = [int(input()) for _ in range(5)]
lst.sort()

res = 0
cnt = 0
for i in range(len(lst)):
    res += lst[i]
    cnt += 1

print(res//cnt)
print(lst[5//2])