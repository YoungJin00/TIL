N = 10
a = [1, 4, 1, 6, 6, 10, 5, 7, 3, 8, 5, 9, 3, 5, 8, 11, 2, 13, 12, 14]
lst = []
for i in range(0, len(a), 2):
    lst.append((a[i], a[i+1]))

lst.sort(key=lambda x: x[1])
cnt = 1
end = lst[0][1]
for i in range(N):
    if end <= lst[i][0]:
        cnt += 1
        end = lst[i][1]
print(lst)
print(cnt)


N = 10
a = [1, 4, 1, 6, 6, 10, 5, 7, 3, 8, 5, 9, 3, 5, 8, 11, 2, 13, 12, 14]
lst = []
for i in range(0, len(a), 2):
    lst.append((a[i], a[i+1]))

lst.sort(key=lambda x: x[1])
lst = [[0,0]] + lst
print(lst)
S = []
j = 0
for i in range(1, N+1):
    if lst[i][0] >= lst[j][1]:
        S.append(i)
        j = i

print(S)