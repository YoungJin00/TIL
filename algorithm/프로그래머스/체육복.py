#코드를 입력하세요.
def solution(n, lost, reserve):
    real_lost = list(set(lost) - set(reserve))
    real_reserve = list(set(reserve) - set(lost))
    
    answer = n - len(real_lost)
    
    for i in real_lost:
        if i - 1 in real_reserve:
            answer += 1
            real_reserve.remove(i-1)
        elif i+1 in real_reserve:
            answer += 1
            real_reserve.remove(i+1)
    return answer