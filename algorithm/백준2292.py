# 벌집

# 1 2 9 22 41 66
#  1 7 13 19 25
#   6 6  6  6 

n = int(input())

bee = 1
res = 1

while n > bee:
    bee += 6 * res
    res += 1

print(res)

