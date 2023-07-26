# 약수들의 합       

while True:
    n = int(input())
    if n == -1:
        break

    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)

    if sum(divisors) == n:
        print(n, "=", " + ".join(str(i) for i in divisors))
    else:
        print(n, "is NOT perfect.")

