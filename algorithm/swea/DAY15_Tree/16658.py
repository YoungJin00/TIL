# subtree
def tree(n):
    global cnt
    if ch1[n]:
        cnt += 1
        tree(ch1[n])
    if ch2[n]:
        cnt += 1
        tree(ch2[n])
    return cnt

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    graph = list(map(int, input().split()))

    ch1 = [0] * (E+2)
    ch2 = [0] * (E+2)

    for i in range(E):
        p, c = graph[i*2], graph[i*2+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
    cnt = 1
    res = tree(N)
    print(f'#{tc} {res}')
