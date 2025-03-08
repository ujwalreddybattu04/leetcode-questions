class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findBound(isFirst):
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    bound = mid  # Store current index
                    if isFirst:
                        right = mid - 1  # Search left for first occurrence
                    else:
                        left = mid + 1  # Search right for last occurrence
                
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return bound
        
        # Find first and last positions using binary search
        first = findBound(True)
        last = findBound(False)
        return [first, last]
