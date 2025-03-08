class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()  # Sort to handle duplicates easily
        
        def backtrack(start, target, path):
            if target == 0:
                res.append(path[:])  # Found a valid combination
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicate elements to avoid duplicate combinations
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > target:
                    break  # No need to continue if current number exceeds target

                # Include candidates[i] and move to the next index
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])

        backtrack(0, target, [])
        return res
