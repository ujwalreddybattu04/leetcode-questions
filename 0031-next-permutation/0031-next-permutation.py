class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        n = len(nums)
        i = n - 2  # Start from second last element
        
        # Step 1: Find first decreasing element from the right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:  # If not entirely descending
            j = n - 1  
            
            # Step 2: Find the smallest element greater than nums[i]
            while nums[j] <= nums[i]:
                j -= 1
            
            # Step 3: Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # Step 4: Reverse the remaining part
        nums[i + 1:] = reversed(nums[i + 1:])

        