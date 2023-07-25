for test_case in range(1,11):
    res = 0
    Count = int(input())
    building = list(map(int , input().split()))
    for i in range(2, Count-2):
        d_2 = building[i] - building[i-2]
        d_1 = building[i] - building[i-1]
        d1 = building[i] - building[i+1]
        d2 = building[i] - building[i+2]
        if d_2 > 0 and d_1 > 0 and d1 > 0 and d2 > 0:
          res += min(d_2, d_1, d1, d2) 
    print(f'#{test_case} {res}')