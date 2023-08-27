# T = int(input())
#
# for tc in range(1, T+1):
#     N, K= map(int, input().split())
#     sample = list(map(int, input().split()))
#     passcode = list(map(int, input().split()))
#
#     sample_idx = 0
#     passcode_idx = 0
#
#     while sample_idx < len(sample) and passcode_idx < len(passcode):
#         if sample[sample_idx] == passcode[passcode_idx]:
#             passcode_idx += 1
#         sample_idx += 1
#
#
#     if passcode_idx == len(passcode):
#         print(f'#{tc} 1')
#     else:
#         print(f'#{tc} 0')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))
    # [ 1, 2, 3, 4 ]
    #   0  1  2 3

    passcode_idx = 0

    for num in sample:
        if num == passcode[passcode_idx]:
            passcode_idx += 1
            if passcode_idx == K:
                break

    if passcode_idx == K:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')







