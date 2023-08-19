N = int(input())
switch = list(map(int, input().split()))

st_num = int(input())

info = []
for _ in range(st_num):
    sung, num = map(int, input().split())
    info.append((sung, num))

for fm, num in info:
    if fm == 1:
        for j in range(N):
            if (j+1) % num == 0:
                switch[j] = 1 - switch[j]

    else:
        num -= 1
        left = num - 1
        right = num + 1

        switch[num] = 1 - switch[num]

        while left >= 0 and right < N:
            if switch[left] == switch[right]:
                switch[left] = 1 - switch[left]
                switch[right] = 1 - switch[right]
                left -= 1
                right += 1
            else:
                break

for i in range(len(switch)):
    if i > 0 and i % 20 == 0:
        print()
    print(switch[i], end=' ')



