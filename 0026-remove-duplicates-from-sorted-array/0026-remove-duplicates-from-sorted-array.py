class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        i = 0  # Pointer for the position of unique elements
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:  # If a new unique element is found
                i += 1
                nums[i] = nums[j]  # Move it to the next position
        
        return i + 1  # Number of unique elements

       
                



        