ma = []

for _ in range(9):
    a = list(map(int, input().split()))
    ma.append(a)

ma_va = 0
row = 0
col = 0

for i in range(9):
    for j in range(9):
        if ma[i][j] > ma_va:
            ma_va = ma[i][j]
            row = i + 1
            col = j + 1

print(ma_va)
print(row, col)