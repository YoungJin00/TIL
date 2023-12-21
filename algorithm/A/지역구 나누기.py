def is_linked(lst):
    Q = [lst[0]]
    while Q:
        v = Q.pop(0)
        for col in range(N):
            if not visited[v] and Rrc[v][col] == 1 and col in lst:
                Q.append(col)
        visited[v] = True


for t in range(1, int(input())+1):
    N = int(input())
    Rrc = [list(map(int, input().split())) for _ in range(N)]
    Pi = list(map(int, input().split()))

    village = list(range(N))
    combine = []
    for i in range(1, 1 << (N-1)):
        temp = []
        temp2 = []
        for j in range(N):
            if i & (1 << j):
                temp.append(village[j])
            else:
                temp2.append(village[j])
        combine.append([temp, temp2])

    MIN = float('inf')
    for C in combine:
        visited = [False] * N
        is_linked(C[0])
        is_linked(C[1])
        if all(visited):
            num1 = sum(Pi[i] for i in C[0])
            num2 = sum(Pi[i] for i in C[1])
            if abs(num2-num1) < MIN:
                MIN = abs(num2-num1)

    print(f'#{t}', MIN)