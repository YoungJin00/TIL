
# 글자수

T = int(input())

for tc in range(1, T+1):
    A = tuple(set(input()))
    B = input()
    num_li = [0] * len(A)
    for i in A:
        for j in range(len(B)):
            if i == B[j]:
                num_li[A.index(i)] += 1

    MAX = 0
    for i in range(len(num_li)):
        if MAX < num_li[i]:
            MAX = num_li[i]

    print(f'#{tc} {MAX}')

# 딕셔너리 활용 풀기
'''
T = int(input())

for tc in range(1, T+1):
    A = input()
    B = input()
    dic = {}

    for i in A:
        if i not in dic.keys():
            dic[i] = 0
    for i in B:
        if i in dic:
            dic[i] += 1
    res = max(dic.values())
    print(f'#{tc} {res}')
'''