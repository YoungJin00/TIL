# 최대 공약수와 최소 공배수

A, B = map(int, input().split())
#
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#
#     return a
#
# def lcm(a, b):
#     return a * b // gcd(a, b)
#
# g1 = gcd(A, B)
# g2 = lcm(A, B)
# print(g1)
# print(g2)

least, greatest = 1, 1
n = 2

while A > 1 or B > 1:
    if A % n == 0 and B % n == 0:
        least *= n
        greatest *= n
        A //= n
        B //= n
    elif A % n == 0 and B % n != 0:
        greatest *= n
        A //= n
    elif A % n != 0 and B % n == 0:
        greatest *= n
        B //= n
    else:
        n += 1

print(least)

