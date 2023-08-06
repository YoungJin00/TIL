n, m = map(int, input().split())

ma1 = []

for _ in range(n):
    row = list(map(int, input().split()))
    ma1.append(row)

ma2 = []

for _ in range(n):
    row = list(map(int, input().split()))
    ma2.append(row)

ma3 = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(ma1[i][j] + ma2[i][j])
    ma3.append(row)

for row in ma3:
    print(''.join(map(str, row)))


