# view
for test_case in range(1,11):
    res = 0
    N = int(input())
    building = list(map(int , input().split()))
    for i in range(2, N-2):
        d_2 = building[i] - building[i-2]
        d_1 = building[i] - building[i-1]
        d1 = building[i] - building[i+1]
        d2 = building[i] - building[i+2]
        if d_2 > 0 and d_1 > 0 and d1 > 0 and d2 > 0:
          res += min(d_2, d_1, d1, d2)
    print(f'#{test_case} {res}')



# for tc in range(1, 11):
#     N = int(input())
#     height = list(map(int, input().split()))

#     view = 0
#     for i in range(2, N-2):
#         max_v = max(height[i-2], height[i-1], height[i+1], height[i+2])
#         if height[i] > max_v:
#             view += height[i] - max_v

#     print(f'#{tc} {view}')

