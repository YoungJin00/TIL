def solution(nums):
    unique_set = set(nums)
    return min(len(unique_set), len(nums) // 2)


def solution(nums):
    ans = 0 
    n_dic = {}
    target = len(nums) / 2
    for n in nums:
        if n in n_dic:
            n_dic[n] += 1
        else:
            n_dic[n] = 1
    for k, v in n_dic.items():
        ans += 1
        if ans == target:
            break    
    return ans