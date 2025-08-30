# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

from typing import List


matrix =[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

def countSquares(matrix: List[List[int]]) -> int:
    if matrix is None or len(matrix) < 1:
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0]*(cols+1) for _ in range(rows+1)]
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1 
    return sum(map(sum, dp))

print(countSquares(matrix))



