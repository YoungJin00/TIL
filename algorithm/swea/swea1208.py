for tc in range(1, 11):
  res = 0
  dump = int(input())
  ct = list(map(int, input().split()))
  for _ in range(dump):
    max_1 = max(ct)
    min_1 = min(ct)
    # 최대, 최소 값 인덱스 받아오기
    maxIdx = ct.index(max_1)
    minIdx = ct.index(min_1)
    ct[maxIdx] -= 1
    ct[minIdx] += 1
  res = max(ct) - min(ct)
  print(f'#{tc} {res}')