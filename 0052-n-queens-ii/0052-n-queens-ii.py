class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_safe(row, col, board):
            for i in range(row):
                if board[i] == col or \
                   board[i] - i == col - row or \
                   board[i] + i == col + row:
                    return False
            return True
        
        def backtrack(row, board):
            nonlocal count
            if row == n:
                count += 1
                return
            
            for col in range(n):
                if is_safe(row, col, board):
                    board[row] = col
                    backtrack(row + 1, board)
                    board[row] = -1
        
        count = 0
        backtrack(0, [-1] * n)
        return count

        