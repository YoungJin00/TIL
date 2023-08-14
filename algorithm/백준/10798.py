words = []
leng = []

for _ in range(5):
    word = input()
    words.append(word)
    leng.append(len(word))

res = ''
for i in range(max(leng)):
    for j in range(5):
        if i < leng[j]:
            res += words[j][i]

print(res)