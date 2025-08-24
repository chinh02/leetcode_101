# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.


from typing import List

cost = [1,100,1,1,1,100,1,1,100,1]

def minCostClimbingStairs(cost: List[int]) -> int:
        if not cost: return 0
        n = len(cost)
        dp = [-1]*n
        dp[0] = cost[0]
        if n >= 2: dp[1] = cost[1]
        for i in range(2,n):
            dp[i] = cost[i] + min(dp[i-1],dp[i-2])
        return min(dp[-2], dp[-1])
 
print(minCostClimbingStairs(cost))