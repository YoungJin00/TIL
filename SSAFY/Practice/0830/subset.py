arr = [3,6,7,1,5,4]
n = len(arr)
                               # 1 << (N-1)이랑도 동일
for i in range(1, (1 << n)-1): # 1 << n : 부분집합의 개수
    subset1 = []
    subset2 = []
    for j in range(n):  # 원소의 수만큼 비트를 비교힘
        if i & (1 << j):     # i의 j번째 비트가 1이면 j번째 원소 출력
            subset1.append(arr[j])
        else:
            subset2.append(arr[j])
    print(subset1, subset2)