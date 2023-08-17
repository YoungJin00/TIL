p = 1 #줄설 '첫번째' 사람번호

q = [] #큐
N = 20 #마이쮸 개수
m = 0 #나눠준 개수


while m < N:
    q.append((p, 1, 0))
    v, c, my = q.pop(0)
    # print(f'큐에 남아있는 사람수{len(q)+1} 받아갈 사탕수{c} 나눠준 사탕수{m}')
    m += c
    q.append((v, c+1, my+c))
    p += 1 #처음 줄서는 사람 번호
print(f'마지막 사탕을 받은사람{v}')