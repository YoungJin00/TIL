# 2798

n, m = list(map(int, input().split()))
data = list(map(int, input().split()))

tot = 0
leng = len(data)

for i in range(leng):
  for j in range(i + 1, leng):
    for k in range(j + 1, leng):
      val = data[i] + data[j] + data[k]
      if val <= m:
        tot = max(tot, val)
print(tot)