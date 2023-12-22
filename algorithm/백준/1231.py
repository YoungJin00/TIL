# 중위순회
def inorder(n):
    global ans
    if n <= N:
        inorder(n *2)
        ans += words[n]
        inorder(n*2+1)

for tc in range(1, 11):
    N = int(input())
    words = [0] * (N+1)
    for i in range(N):
        lst = list(input().split())
        words[i+1] = lst[1]
    ans = ''
    inorder(1)
    print(f'#{tc} {ans}')
