class Solution:
    def twoSum(self,nums,target):
     store = {}  
     for i, num in enumerate(nums):
        required = target-num
        if required in store:
            return [store[required], i]
        store[num] = i  


  
