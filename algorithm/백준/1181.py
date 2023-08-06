# 단어정렬

N = int(input())
li = []
for i in range(N):
    li.append(input())
set_li = list(set(li))

sort_li = []
for i in set_li:
    sort_li.append((len(i), i))

sort_li.sort()
for i, j in sort_li:
    print(j)



