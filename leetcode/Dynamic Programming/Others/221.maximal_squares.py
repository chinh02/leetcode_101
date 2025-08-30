# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

from typing import List


matrix = [[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]


def maximalSquare(matrix: List[List[int]]):
    max_side_length = 0
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0]*(cols+1) for _ in range(rows+1)]
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1
                max_side_length = max(dp[r+1][c+1], max_side_length)
    return max_side_length * max_side_length

print(maximalSquare(matrix))