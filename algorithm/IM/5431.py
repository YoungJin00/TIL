# 민석이의 과제 체크하기
T = int(input())
for tc in range(1, T+1):
    n, k = map(int,input().split())
    student = list(range(1,n+1))
    lst = sorted(map(int, input().split()))

    for i in range(k):
        student.remove(lst[i])

    print(f'#{tc}', *student)