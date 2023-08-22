# 노드의 합

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)

    for _ in range(M):
        a, b = map(int, input().split())
        tree[a] = b

    for i in range(N-M, 0, -1):
        if i * 2 + 1 <= N:  # 왼쪽과 오른쪽 자식 노드가 모두 존재하는 경우
            tree[i] = tree[i*2] + tree[i*2+1]
        else:  # 왼쪽 자식만 있는 경우
            tree[i] = tree[i*2]

    print(f'#{tc} {tree[L]}')