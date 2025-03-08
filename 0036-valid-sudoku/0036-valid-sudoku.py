class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue  # Skip empty cells
                
                box_index = (r // 3) * 3 + (c // 3)  # Identify 3×3 sub-box
                
                if num in rows[r] or num in cols[c] or num in boxes[box_index]:
                    return False  # Found duplicate
                
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)
        
        return True
