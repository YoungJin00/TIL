# 회문

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     words = [input() for _ in range(N)]
#     w_li = []
#     # 가로 확인
#     for w in words:
#         for i in range(N-M+1):
#             cnt = 1
#             for j in range(M//2):
#                 if w[i+j] != w[i+M-1-j]:
#                     cnt = 0
#                     break
#             if cnt == 1:
#                 w_li.append(w[i:i+M])

#     # 세로 확인
#     col_words = [''.join(row) for row in zip(*words)]
#     for c in col_words:
#         for i in range(N-M+1):
#             cnt = 1
#             for j in range(M // 2):
#                 if c[i+j] != c[i+M-1 - j]:
#                     cnt = 0
#                     break
#             if cnt == 1:
#                 w_li.append(c[i:i+M])
#     print(f'#{tc}', *w_li)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    leng = len(arr) // 2
    
    w_li = []
    # 가로 확인
    for w in arr:
        for i in range(N-M+1):
            cnt = 1
            for j in range(M//2):
                if w[i+j] != w[i+M-1-j]:
                    cnt = 0
                    break
            if cnt == 1:
                w_li.append(w[i:i+M])
                
    print(w_li)




