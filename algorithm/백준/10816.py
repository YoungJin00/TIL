N = int(input())
N_lst = sorted(map(int, input().split()))

M = int(input())
M_lst = list(map(int, input().split()))

M_dic = dict.fromkeys(M_lst, 0)

for i in M_lst:
    for j in N_lst:
        if i == j:
            M_dic[i] += 1

for i in M_dic.values():
    print(i, end=' ')