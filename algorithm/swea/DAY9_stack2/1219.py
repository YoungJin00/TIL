# 길찾기
def DFS(n, g, lst):
    stack = []  # stack 생성
    visited = [0] * 101  # visited 생성
    visited[n] = 1  # 시적점 방문 위치

    while True:
        for w in range(100):
            if n == g:
                return 1

            if lst[n][w] == 1 and visited[w] == 0:
                stack.append(n)
                n = w
                # print(n, end=' ')
                visited[n] = 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break

    return 0

for _ in range(1, 11):
    tc, V = map(int, input().split())
    MAP = list(map(int, input().split()))
    MAP100 = [[0] * 100 for _ in range(100)]

    for i in range(len(MAP) // 2):
        v1, v2 = MAP[i*2], MAP[i*2+1]
        MAP100[v1][v2] = 1

    print(f'#{tc}', DFS(0, 99, MAP100))