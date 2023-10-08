for t in range(1, int(input())+1):
    N = int(input())
    trees = list(map(int, input().split()))
    target = max(trees)
    grow =[target-tree for tree in trees]

    odd = 0
    even = 0
    for need in grow:
        odd += need % 2
        even += need // 2

    day = 0
    while odd+1 < even:
        odd += 2
        even -= 1

    if odd > even:
        day += (2*odd)-1
    else:
        day += even * 2


    print(f'#{t}', day)