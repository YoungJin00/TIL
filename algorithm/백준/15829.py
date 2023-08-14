L = int(input())
st = input()
ans = 0

for i in range(L):
    ans += (ord(st[i]) - 96) * (31 ** i)

print(ans % 1234567891)