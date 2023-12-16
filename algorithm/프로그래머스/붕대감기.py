def solution(bandage, health, attacks):
    # 초기 health값 넘어가지 않게 max_health로 할당
    max_health = health
    # 마지막 공격 시간을 할당
    max_time = attacks[-1][0]
    attack_dict = {}
    for i in attacks:
        attack_dict[i[0]] = i[1]

    continue_sec, t = 0, 0

    while t <= max_time:
        if t in attack_dict:
            health -= attack_dict[t]
            continue_sec=0

            # 공격을 맞고 체력이 0 이하이면 -1 리턴
            if health <=0:
                return -1

        else:
            continue_sec += 1
            if continue_sec < bandage[0]:
                health += bandage[1]
                if health>max_health:
                    health = max_health

            else:
                health = health + bandage[1] + bandage[2]
                if health>max_health:
                    health = max_health
                continue_sec=0

        t+=1

    return health

result = solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]])
print(result)