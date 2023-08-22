def inorder(p, N):  # N 마지막 정점
    if p <= N:
        inorder(p*2, N)
        print(tree[p], end='')
        inorder(p*2+1, N)

T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1) # N번 노드까지 있는 완전이진트리

    for _ in range(N):
        lst = list(input().split())
        tree[int(lst[0])] = lst[1]

    # 중위 순회
    print(f'#{tc}', end=' ')
    inorder(1, N)
    print()
