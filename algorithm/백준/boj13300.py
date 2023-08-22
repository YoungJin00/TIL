# 방배정

num_student, max_room = map(int, input().split()) # 학생 수, 방 최대 입장인원

w = [0] * 7
m = [0] * 7

for i in range(num_student):
    # S: 성별 ( 0: 여, 1:남) , 학년
    S, Y = map(int, input().split())
    if S == 0:
        w[Y] += 1
    else:
        m[Y] += 1

res = 0
for i in range(1, 7):
    res += (w[i] + max_room - 1) // max_room # 나눳을때 나머지가 생기지 않고 딱 떨어짐
    res += (m[i] + max_room - 1) // max_room

print(res)

