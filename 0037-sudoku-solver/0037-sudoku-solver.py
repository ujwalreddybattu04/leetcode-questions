class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        def isValid(row, col, num):
            """Check if placing 'num' at board[row][col] is valid."""
            box_index = (row // 3) * 3 + (col // 3)
            
            if num in rows[row] or num in cols[col] or num in boxes[box_index]:
                return False
            return True

        def backtrack(row=0, col=0):
            """Backtracking function to solve Sudoku."""
            if row == 9:  # All rows filled
                return True
            
            if col == 9:  # Move to next row
                return backtrack(row + 1, 0)
            
            if board[row][col] != ".":  # Skip filled cells
                return backtrack(row, col + 1)
            
            for num in map(str, range(1, 10)):  # Try numbers 1-9
                if isValid(row, col, num):
                    board[row][col] = num
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[(row // 3) * 3 + (col // 3)].add(num)
                    
                    if backtrack(row, col + 1):  # Recursively solve next cell
                        return True
                    
                    # Undo choice (Backtrack)
                    board[row][col] = "."
                    rows[row].remove(num)
                    cols[col].remove(num)
                    boxes[(row // 3) * 3 + (col // 3)].remove(num)
            
            return False  # No valid number found, backtrack

        # Initialize sets for rows, columns, and 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # Populate existing numbers into sets
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num != ".":
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + (c // 3)].add(num)
        
        backtrack()  # Start solving

        