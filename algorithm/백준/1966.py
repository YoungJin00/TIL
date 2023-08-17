from queue import PriorityQueue
# q = PriorityQueue(maxsize=8)
T = int(input())
for _ in range(T):
    # N : 문서의 개수, M 몇 번째 놓여있는지
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    lst = [(i, idx) for idx, i in enumerate(lst)]

    cnt = 0
    while True:
        if lst[0][0] == max(lst, key=lambda x: x[0])[0]:
            cnt += 1
            if lst[0][1] == M:
                print(cnt)
                break
            else:
                lst.pop(0)
        else:
            lst.append(lst.pop(0))







