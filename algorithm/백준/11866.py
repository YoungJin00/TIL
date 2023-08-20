n, k = map(int, input().split())

lst = [i for i in range(1, n+1)]
res = []
idx = 0
while len(lst) > 0:
    idx += (k-1)
    idx = idx % (len(lst))
    res.append(lst.pop(idx))

print("<", end='')
for i in range(n-1):
    print(res[i], end=', ')
print(res[-1], end='')
print(">")

