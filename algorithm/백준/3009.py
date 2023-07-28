# 네번쨰점

cnt = 0
ls = []
for _ in range(3):
    a, b = input().split()
    ls.append(a)
    ls.append(b)

one = ls.count(a)
two = ls.count(b)

if one != 4 and two != 4:
    print(a, b)
elif one == 4 and two != 4:
    print(b, b)
else:
    print(a, a)


