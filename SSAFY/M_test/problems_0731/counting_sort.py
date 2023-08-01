# data = [7, 6, 7, 1, 1, 2, 4, 3]
# counts = [0]*10
# N = len(data)
# tmp = [0] * N
# for x in data:
#     counts[x] += 1
# # print(counts)
# for i in range(1,10):
#     counts[i] += counts[i-1]
# print(counts)
# for i in range(N-1, -1, -1):
#     counts[data[i]] -= 1
#     tmp[counts[data[i]]] = data[i]
#
# print(tmp)
