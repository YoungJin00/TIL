"""
0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 떄, 3장의 카드가 연속적인 번호를
갖는 경우 run, 3장의 카드가 동일한 번호를 갖는 경우를 triplet
"""

def run1(lst):
    lst_sort = sorted(set(lst))
    for j in range(len(lst_sort) - 2):
        if lst_sort[j] + 1 == lst_sort[j + 1] and lst_sort[j + 1] + 1 == lst_sort[j + 2]:
            return True
    return False


def tri(lst):
    for w in lst:
        if lst.count(w) == 3:
            return True
    return False


T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    A = []
    B = []
    for i in range(0, len(cards), 2):
        A.append(cards[i])
        B.append(cards[i+1])
        if i >= 4:
            if run1(A) or tri(A):
                print(f'#{tc}', 1)
                break
        if i >= 4:
            if run1(B) or tri(B):
                print(f'#{tc}', 2)
                break
    else:
        print(f'#{tc}', 0)











