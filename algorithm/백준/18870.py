# 좌표압축
import sys

input = sys.stdin.readline

# N = int(input())
# lst = list(map(int, input().split()))
#
# res = []
#
# # 좌표 압축을 수행하고 결과를 리스트에 저장
# for i, num in enumerate(lst):
#     cnt = 0
#     for j, num2 in enumerate(lst):
#         if i != j and num > num2:
#             cnt += 1
#     res.append(cnt)
#
# print(*res)

n = int(input())

lst = list(map(int, input().split()))

# 중복 제거 및 오름차순 정렬한 리스트 생성
sorted_lst = sorted(list(set(lst)))

# 좌표 압축 결과를 저장할 딕셔너리 생성
dic = {}
for i in range(len(sorted_lst)):
    num = sorted_lst[i]
    dic[num] = i

# 원본 데이터를 순회하면서 좌표 압축된 값을 출력
for num in lst:
    print(dic[num], end=' ')
