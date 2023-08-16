# 덩치
N = int(input())

lst =[]
for _ in range(N):
    x, y =list(map(int, input().split()))
    lst.append((x,y))


for a in lst:
    rank = 1
    for b in lst:
        if a[0] < b[0] and a[1] < b[1]:
            rank += 1
    print(rank, end=' ') 
    
    

    
    