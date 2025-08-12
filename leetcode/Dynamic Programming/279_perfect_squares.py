# Given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.

# Input: n = 13
# Output: 2
# Explanation: 12 = 4 + 9.

n = 13

def perfect_squares(n: int) -> int:
    count = 1
    dp = [float('inf')]* (n+1)
    dp[0] = 0
    while count * count <= n:
        square = count * count
        for i in range(square, n+1):
            dp[i] = min(dp[i], dp[i-square]+1)
        count += 1  
    return dp

print(perfect_squares(n))