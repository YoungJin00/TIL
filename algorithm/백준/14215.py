# 14215 세 막대
# sorted 함수의 결과가 리스트라서

li = sorted(map(int, input().split()))
res = li[0] + li[1] + min(li[2], li[0]+li[1]-1)
print(res)