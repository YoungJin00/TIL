# 화물도크
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = []
    for _ in range(N):
        a, b = map(int, input().split())
        lst.append((a, b))
    lst.sort(key=lambda x: x[1])
    cnt = 1 # 첫번째 화물차 무조건 선택 가능
    end = lst[0][1]

    for i in range(1, N):
        if lst[i][0] >= end: # 다음 화물차의 도착 시간이 이전 화물차의 출발 시간보다 크거나 같으면 선택 가능
            cnt += 1
            end = lst[i][1]  # 현재 화물차 출발 시간 업데이트
    print(f'#{tc} {cnt}')