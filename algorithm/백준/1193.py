# 분수찾기

n = int(input())

line = 1

while n > line:
    n -= line
    line += 1

# 짝수 라인인 경우: 분모 -1, 분자는  +1
if line % 2 == 0:
    ja = n
    mo = line - n + 1
    
# 홀수 : 분모 +1, 분자 감소
else:
    ja = line - n + 1
    mo = n
    
print(f'{ja}/{mo}')

