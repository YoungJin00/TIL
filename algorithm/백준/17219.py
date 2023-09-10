# 비밀번호 찾기
import sys

N, M = map(int, sys.stdin.readline().split())

email_pw = {}
for _ in range(N):
    email, pw = sys.stdin.readline().split()
    email_pw[email] = pw

for _ in range(M):
    id = sys.stdin.readline().rstrip('\n')
    print(email_pw[id])


