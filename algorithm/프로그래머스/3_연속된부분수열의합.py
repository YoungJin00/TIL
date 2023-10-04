def solution(seq, k):
    start, end, total = 0, 0, seq[0]
    seq += [0]  # 입력 시퀀스의 끝에 0을 추가하여 반복문 종료 조건을 처리할 수 있도록 합니다.
    first, second = 1000000, 2000000  # 초기 최소 길이 설정

    while end < len(seq) - 1:
        if total <= k:
            # 현재 부분 시퀀스의 합이 k 이하인 경우
            if total == k and end - start < second - first:
                # 부분 시퀀스의 합이 k와 같으며, 현재 길이가 최소 길이보다 짧은 경우
                first, second = start, end  # 현재 부분 시퀀스를 최소 길이로 업데이트
            end += 1  # 부분 시퀀스의 끝 지점을 오른쪽으로 이동
            total += seq[end]  # 새로운 원소를 부분 시퀀스 합에 추가
        else:
            start += 1  # 부분 시퀀스의 시작 지점을 오른쪽으로 이동
            total -= seq[start - 1]  # 이전 시작 원소를 부분 시퀀스 합에서 제거

    return [first, second]


print(solution([1, 2, 3, 4, 5], 7))