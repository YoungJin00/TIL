"""
0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 떄, 3장의 카드가 연속적인 번호를
갖는 경우 run, 3장의 카드가 동일한 번호를 갖는 경우를 triplet
"""

num = 456789
c = [0] * 12

for i in range(6):
    c[num % 10] += 1
    num //= 10

i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3:
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i+1] >=1 and c[i+2] >= 1:
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1
if run + tri == 2: print("Baby Gin")
else: print("Lose")
