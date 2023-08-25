# 암호코드 스캔

hex_to_bin = {
    '0':'0000', '1':'0001', '2':'0010', '3':'0011',
    '4':'0100', '5':'0101', '6':'0110', '7':'0111',
    '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
    'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'
}

DICT = {
    "211": 0, "221": 1, "122": 2,
    "411": 3, "132": 4, "231": 5,
    "114": 6, "312": 7, "213": 8,
    "112": 9
}

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [input().strip() for _ in range(N)]
    SET = set(lst)
    result = set()
    newSet = set()

    for s in SET:
        if not all(c == '0' for c in s):
            newSet.add(s)

    for ns in newSet:
        binaryString = ''
        for char in ns:
            binaryString += hex_to_bin[char]

        start = 0
        countArray = []
        for i in range(len(binaryString)):
            if binaryString[i] != binaryString[start]:
                countArray.append(i - start)
                start = i

        pwd = []
        for i in range(1, len(countArray), 4):
            mn = min(countArray[i:i+3])
            key = str(countArray[i]//mn) + str(countArray[i+1]//mn) + str(countArray[i+2]//mn)
            pwd.append(DICT[key])

        for i in range(0, len(pwd), 8):
            result.add(tuple(pwd[i:i+8]))

    res = 0
    for r in result:
        if (sum(r[0:8:2]) * 3 + sum(r[1:8:2])) % 10 == 0:
            res += sum(r)

    print(f'#{t} {res}')