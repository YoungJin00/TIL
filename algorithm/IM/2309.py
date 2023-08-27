lst = []
for i in range(9):
    n =int(input())
    lst.append(n)
lst.sort()
f = sum(lst) - 100
for i in range(9):
    for j in range(i+1, 9):
        if lst[i] + lst[j] == f:
            a = lst[i]
            b = lst[j]
            break

lst.remove(a)
lst.remove(b)

for i in lst:
    print(i)

