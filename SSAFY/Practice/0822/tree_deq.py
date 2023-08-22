def deq():
    global last
    tmp = heap[1]   # 루트 백업
    heap[1] = heap[last]    # 삭제할 노드의 키를 루트에 복사
    last -= 1   # 마지막 노드 삭제
    p = 1  # 루트에 옮긴 값을 자식과 비교
    c = p * 2  # 왼쪽 자식 (비교할 자식노드 번호)
    while c <= last:  # 자식이 하나라도 있으면...
        if c+1 <= last and heap[c] < heap[c + 1]:  # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면
            c += 1      # 비교 대상이 오른쪽 자식노드
        else:  # 부모가 더 크면
            break  # 비교 중단

    return tmp

heap = [0] * 100
last = 0  # 마지막 정점 번호