# 베스트셀러
N = int(input())
books = {}

for _ in range(N):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

MAX = max(books.values())

lst = []
for key, val in books.items():
    if val == MAX:
        lst.append(key)
lst.sort()
print(lst[0])



