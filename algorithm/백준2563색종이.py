# 색종이 수
N = int(input())
# 색종이 위치 받아오기
arr = [[0] * 100 for _ in range(100)]

for _ in range(N):
  a, b = list(map(int, input().split()))

  for i in range(a, a+10):
    for j in range(b, b+10):
      arr[i][j] = 1

res = 0
for c in range(100):
  res += arr[c].count(1)

print(res)

