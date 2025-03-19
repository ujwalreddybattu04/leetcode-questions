from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()  # Sort to handle duplicates

        def backtrack(start, current_combination, remaining_target):
            if remaining_target == 0:
                result.append(list(current_combination))
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # Skip duplicates
                if candidates[i] > remaining_target:
                    break  # Stop if the number exceeds the remaining target
                current_combination.append(candidates[i])
                backtrack(i + 1, current_combination, remaining_target - candidates[i])
                current_combination.pop()  # Backtrack

        backtrack(0, [], target)
        return result
