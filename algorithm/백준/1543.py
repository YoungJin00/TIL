# 문서검색

words = input()
find_word = input()

idx = 0
res = 0

while len(words) - idx >= len(find_word):
    if words[idx:idx+len(find_word)] == find_word:
        res += 1
        idx += len(find_word)
    else:
        idx += 1
print(res)

