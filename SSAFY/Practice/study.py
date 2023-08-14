# 소수 찾기
n = 10
for x in range(2, n+1):
  is_prime = True
  for y in range(2, x):
    if x % y == 0:
      print(x, "=", y, '*', x // y)
      is_prime = False
      break
  if is_prime:
    print(x, "는 소수입니다.")

## test 한번
## test 두번
