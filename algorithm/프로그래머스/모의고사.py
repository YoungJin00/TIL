def solution(answers):
    answer=[]
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    
    r1,r2,r3 = 0, 0, 0
    
    for i in range(len(answers)):
        if answers[i] == a1[i%len(a1)]:
            r1 += 1
        if answers[i] == a2[i%len(a2)]:
            r2 += 1
        if answers[i] == a3[i%len(a3)]:
            r3 += 1
    target = max(r1,r2,r3)
    
    if target == r1:
        answer.append(1)
    if target == r2:
        answer.append(2)
    if target == r3:
        answer.append(3)
    
    return answer