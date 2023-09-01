# T = int(input())
# for tc in range(1, T+1):
#     A = input()
#     B = list(map(int, input()))
#
#     N = len(A)
#     M = len(B)
#     ans = 0
#
#     binary = int(A, 2)
#     bin_list = [0] * N
#     for i in range(N):
#         bin_list[i] = binary ^ (1<<i)
#
#     for i in range(M):
#         num1 = 0
#         num2 = 0
#         for j in range(M):
#             if i != j:
#                 num1 = num1 * 3 + B[j]
#                 num2 = num2 * 3 + B[j]
#             else:
#                 num1 = num1 * 3 + (B[j]+1) % 3
#                 num2 = num2 * 3 + (B[j]+2) % 3
#
#         if num1 in bin_list:
#             ans = num1
#             break
#         if num2 in bin_list:
#             ans = num2
#             break
#
#     print(ans)


T = int(input())

for t in range(1, T+1):
    lst2 = list(map(int,input()))
    lst3 = list(map(int,input()))

    #이문제를 어떻게 풀것인가?
    # 2진수,3진수 -> 진법변환
    # "한"자리만 틀렸다


    for i in range(len(lst2)):
        lst2[i] = (lst2[i] + 1) % 2

        #2진수 리스트를 -> 10진수로 변경
        decimal = 0
        for n in lst2:
            # print("계산전", i, n, decimal)
            decimal = decimal * 2 + n
            # print("계산후", i,n,decimal)
        # print(decimal)

        #10진수들을 -> 3진수
        temp = []
        test = decimal
        cnt = 0



        while test > 0:
            # print("기존의 test",test)
            temp.insert(0, test % 3)
            test //= 3
            # print(test)



        tempReverse,lstReverse = temp[::-1] , lst3[::-1]

        for j in range(min(len(temp),len(lst3))):
            if tempReverse[j] != lstReverse[j]:
                cnt += 1

        cnt += abs(len(tempReverse) - len(lstReverse))

        if cnt == 1:
            result = decimal

        #비교
        #틀린 자리수가 1"인"경우만
        lst2[i] = (lst2[i] + 1) % 2 #원복

    print(f'#{t} {result}')


