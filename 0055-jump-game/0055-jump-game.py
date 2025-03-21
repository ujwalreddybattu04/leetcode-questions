from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        for i, jump in enumerate(nums):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + jump)
        return True

# Example Test
nums = [2, 3, 1, 1, 4]
solution = Solution()
print(solution.canJump(nums))  # Output: True
