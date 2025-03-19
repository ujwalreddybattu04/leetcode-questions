from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(row, col, board):
            for i in range(row):
                if board[i] == col or \
                   board[i] - i == col - row or \
                   board[i] + i == col + row:
                    return False
            return True
        
        def backtrack(row, board):
            if row == n:
                result.append(["".join("Q" if board[i] == j else "." for j in range(n)) for i in range(n)])
                return
            
            for col in range(n):
                if is_safe(row, col, board):
                    board[row] = col
                    backtrack(row + 1, board)
                    board[row] = -1
        
        result = []
        backtrack(0, [-1] * n)
        return result

        