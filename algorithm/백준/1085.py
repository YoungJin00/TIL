# 직사각형에서 탈출
x, y, w, h = map(int, input().split())

row1 = min(w - x, h - y)
row2 = min(x-0, y-0)

if row1 > row2:
    print(row2)
else:
    print(row1)

