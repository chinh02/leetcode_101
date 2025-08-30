# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

from collections import defaultdict
from typing import List

board =[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def isValidSudoku(matrix: List[List[str]])->bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    box = defaultdict(set)
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == ".": continue
            if matrix[r][c] in rows[r] or matrix[r][c] in cols[c] or matrix[r][c] in box[(r//3,c//3)]:
                return False
            else:
                rows[r].add(matrix[r][c])
                cols[c].add(matrix[r][c])
                box[(r//3,c//3)].add(matrix[r][c])  
    return True


print(isValidSudoku(board))