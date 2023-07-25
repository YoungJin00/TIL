# 달팽이는 올라가고 싶다.

a, b, v = map(int, input().split())

day = ( v - b - 1) // ( a - b ) + 1

print(day)