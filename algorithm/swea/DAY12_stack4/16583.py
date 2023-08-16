# 토너먼트 카드게임

'''
가위바위보 그려진 카드 토너먼트로 한명 뽑기
1번 부터 N번까지 N 명의 학생이 N장의 카드를 나눠 가짐
전체를 두 개의 그룹으로 나누고
그룹의 승자는 그룹내부를 다시 두 그룹으로 나눠뽑기
i ~ j 까지 속한 그룹은 파이썬 연산으로 나눔
i , (i+j)//2  | (i+j) // 2+1, j

1 : 가위
2 : 바위
3 : 보
같은 경우 번호작은사람 이김

input
3
4
1 3 2 1
6
2 1 1 2 3 3
7
1 3 3 3 1 1 3

'''
def divide(i, j):
    if i == j:
        return i
    g1 = divide(i, (i+j)//2)
    g2 = divide((i+j) // 2+1, j)

    return rsp(g1, g2)

def rsp(a, b):
    # 비겼을 때
    if card[a] == card[b]:
        return a
    # a가 이기는 경우
    elif card[a] - card[b] == 1 or card[a] - card[b] == -2:
        return a
    # b가 이기는 경우
    return b

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))
    res = divide(0, N-1)

    print(f'#{tc} {res+1}')

