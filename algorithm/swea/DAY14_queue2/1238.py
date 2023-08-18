# Contact

def bfs(s):
    visited = [0] * 101  # visited 생성
    q = [s]  # 인큐 생성
    visited[s] = 1  # 방문 1 변환

    while q:
        s = q.pop(0)  # 디큐

        for i in contact[s]:
            if not visited[i]:  # 인접리스트에 존재하지않으면
                q.append(i)  # 큐에 i 추가
                visited[i] = visited[s] + 1

                # 리스트에서 최대값을 찾아 인덱스 찾기
    max_val = float('-inf')
    max_idx = -1

    for idx, val in enumerate(visited):
        if max_val <= val:
            max_val = val
            max_idx = idx
    return max_idx


for tc in range(1, 11):
    N, s = map(int, input().split())
    num = list(map(int, input().split()))

    contact = [[] for _ in range(101)]
    for i in range(0, N, 2):
        v1, v2 = num[i], num[i + 1]
        contact[v1].append(v2)

    ans = bfs(s)

    print(f'#{tc} {ans}')