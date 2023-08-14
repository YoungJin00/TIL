# 배수와 약수
while 1:
    b, c = map(int, input().split())
    if b == 0 and c == 0:
        break
    if b >= c:
        if b % c == 0:
            print('multiple')
        else:
            print('neither')
    elif b <= c:
        if c % b == 0:
            print('factor')
    
    
               
         