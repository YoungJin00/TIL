# 나이순 정렬
T = int(input())
li = []

for tc in range(T):
    age, name =  input().split()
    age = int(age)
    li.append((age, name))

li.sort(key= lambda x : x[0])

for i in li:
    print(i[0], i[1])
