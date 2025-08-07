# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed
# the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected 
# and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each housem,
# return the maximum amount of money you can rob tonight without alerting the police.

# result = max(nums[i-2]+nums[i], nums[i-1])
from typing import List


# nums = [1,2,3,1]

nums = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]

def rob_brute_force(nums: List[int]) -> int:
    def helper(i: int) -> int:
        if i < 0:
            return 0
        return max(helper(i - 2) + nums[i], helper(i - 1))
    
    return helper(len(nums) - 1)


def rob_recursive_with_memo(nums: List[int]) -> int:
    n = len(nums)
    memo = [-1] * n

    def dp(i: int) -> int:
        if i < 0:
            return 0
        if memo[i] >= 0:
            return memo[i]
        
        # Choose to rob current house or skip it
        result = max(dp(i - 1), dp(i - 2) + nums[i])
        memo[i] = result
        return result

    return dp(n - 1)

def rob_iterative_with_memo(nums: List[int]) -> int:
    n = len(nums)
    if n == 0: return 0
    if n == 1: return nums[0]
    dp = [0]*n

    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])
    return dp[-1]

def rob_iterate_2_var(nums: List[int]) -> int:
    n = len(nums)
    if n == 0: return 0
    prev_1 = 0
    prev_2 = 0
    for i in range(n):
        tmp = prev_1
        prev_1  = max(prev_1+nums[i], prev_2)
        prev_2 = tmp
    return prev_1
    
print(rob_brute_force(nums)) 
print(rob_recursive_with_memo(nums)) 
print(rob_iterative_with_memo(nums)) 
print(rob_iterate_2_var(nums)) 