from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(start, current_combination, remaining_target):
            if remaining_target == 0:
                result.append(list(current_combination))  # Store a valid combination
                return
            if remaining_target < 0:
                return  # Stop if sum exceeds target

            for i in range(start, len(candidates)):
                current_combination.append(candidates[i])
                backtrack(i, current_combination, remaining_target - candidates[i])  # Same index allows reusing
                current_combination.pop()  # Backtrack

        backtrack(0, [], target)
        return result
