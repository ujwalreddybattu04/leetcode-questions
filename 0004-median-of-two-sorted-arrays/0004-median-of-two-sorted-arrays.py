from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_nums =nums1+nums2
        sorted_nums.sort()
        n=len(sorted_nums)
        mid=n//2
        if n%2==0:
            median=(sorted_nums[mid-1]+sorted_nums[mid])/2 
        else:
            median=sorted_nums[mid]  
        return median

        