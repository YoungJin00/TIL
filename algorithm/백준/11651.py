# 좌표 정렬하기2

N = int(input())
lst = []
for _ in range(N):
    x, y = list(map(int, input().split()))
    lst.append((y,x))

sort_lst = sorted(lst)

# 1
for y, x in sort_lst:
    print(x, y)

# 2 시간초과
# for i in range(N):
#     print(sort_lst[i][1], sort_lst[i][0])
   
   
   
   
   
   
   
            