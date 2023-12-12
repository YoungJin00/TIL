from itertools import combinations

def isValid(lst):
    for i in range(3):
        diff = lst[(i+1)] - lst[i]
        if diff == 1 or diff == N - 1:
            return False
    diff = lst[3] - lst[0]
    if diff == N-1:
        return False
    return True


def validity(lst):
    temp1 = (lst[0] + lst[1])**2 + (lst[2] + lst[3])**2
    temp2 = (lst[0] + lst[3])**2 + (lst[1] + lst[2])**2
    return max(temp1, temp2)


choose = list(combinations([0, 1, 2, 3, 4, 5, 6, 7], 4))
T = int(input())
for t in range(1, T+1):
    N = int(input())
    temp = list(map(int, input().split()))
    stations = dict()
    for idx, val in enumerate(temp):
        stations[idx] = val

    idx = [*range(N)]
    idx.sort(key=lambda x: -stations[x])

    result = 0
    for index in choose:
        candidates = sorted([idx[i] for i in index])
        if isValid(candidates):
            passengerNums = [stations[i] for i in candidates]
            result = max(validity(passengerNums), result)

    print(f'#{t} {result}')