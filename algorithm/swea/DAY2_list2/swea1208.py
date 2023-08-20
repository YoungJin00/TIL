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
  

# for tc in range(1, 11):
#     dump = int(input())
#     boxes = list(map(int, input().split()))

#     for _ in range(dump):
#         boxes.sort()
#         if boxes[-1] - boxes[0] <= 1:
#             break
#         boxes[0] += 1
#         boxes[-1] -= 1

#     res = max(boxes) - min(boxes)

#     print(f'#{tc} {res}')
  

# 내장함수 안쓰고 풀어보기

# for tc in range(1, 11):
#     N = int(input())
#     dump = list(map(int, input().split()))

#     ans = 0
#     while N > 0:
#         N -= 1
#         max_idx = 0
#         min_idx = 0
#         for i in range(1, 100):
#             if dump[min_idx] > dump[i]: # 가장 낮은곳
#                 min_idx = i
#             if dump[max_idx] < dump[i]: # 가장 높은 곳
#                 max_idx = i
#         if dump[max_idx] - dump[min_idx] < 2:
#             ans = dump[max_idx] - dump[min_idx]
#             break
#         else:
#             dump[max_idx] -= 1
#             dump[min_idx] += 1
#     if N == 0 :
#         max_idx = 0
#         min_idx = 0
#         for i in range(100):
#             if dump[min_idx] > dump[i]:  # 가장 낮은곳
#                 min_idx = i
#             if dump[max_idx] < dump[i]:  # 가장 높은 곳
#                 max_idx = i

#         ans = dump[max_idx] - dump[min_idx]

#     print(f'#{tc} {ans}')


