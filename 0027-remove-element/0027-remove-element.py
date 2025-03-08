class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0  # Pointer to track non-val elements
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]  # Move valid element forward
                i += 1
        return i  # Number of valid elements

        