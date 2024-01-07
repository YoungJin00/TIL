f = ["muzi", "ryan", "frodo", "neo"]
gg = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

dic = { f:i for i, f in enumerate(f)}
table = [[0] * len(f) for _ in range(len(f))]
res = [0] * len(f)

for gift in gg:
    g, t = gift.split()
    table[dic[g]][dic[t]] += 1

p_given = [sum(row) for row in table]
p_taken = [sum(col) for col in zip(*table)]
jisu = [p_given[i] - p_taken[i] for i in range(len(f))]

for i in range(len(f)):
    for j in range(i + 1, len(f)):
        if table[i][j] > table[j][i]:
            res[i] += 1
        elif table[i][j] < table[j][i]:
            res[j] += 1
        else:
            if jisu[i] > jisu[j]:
                res[i] += 1
            elif jisu[j] > jisu[i]:
                res[j] += 1
        
print(max(res))

# res = 2