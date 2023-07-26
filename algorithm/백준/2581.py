# 소수
a = int(input())
b = int(input())   
    
li = []
    
for i in range(a, b+1):
    if i < 2:
        continue
    is_prime = True
    for j in range(2, int(i ** 0.5)+1):
        if i % j == 0:
            is_prime = False
            break
    
    if is_prime:
        li.append(i)

if not li:
    print('-1')
else:
    print(sum(li))
    print(min(li))       
            

    
