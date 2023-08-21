def inorder(n):
    if n:
        inorder(ch1[n])   # 왼쪽서브트리로 이동
        print(n, end=' ')    # visit(n)
        inorder(ch2[n])   # 오른쪽 서브트리로 이동



for tc in range(1, 11):
    N = int(input())
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    lst = []
    for _ in range(N):
        lst.append(input().split())

    # for i in range(N-1):
    #     if ch1[] == 0:  # 자식 1이 아직 없으면
    #         ch1[p] = c
    #     else:
    #         ch2[p] = c

    print(lst)



    # if ch1[i] == 0:
    #     ch1[i] = lc
    # else:
    #     ch2[i] = rc

    # print(ch1)
    # print(ch2)

