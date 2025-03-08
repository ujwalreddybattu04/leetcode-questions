class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2  # Find middle index
            
            if nums[mid] == target:
                return mid  # Found target
            
            if nums[mid] < target:
                left = mid + 1  # Move right
            else:
                right = mid - 1  # Move left
        
        return left  # Return insert position
