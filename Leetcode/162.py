"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Your solution should be in logarithmic complexity.
"""

import sys
class Solution(object):
    def recursive(self, start, end, nums):
        if start >= end:
            if nums[start]>(nums[start-1] if start-1 >=0 else -sys.maxsize) \
                and nums[start]>(nums[start+1] if start+1<len(nums) else -sys.maxsize):
                return start
            else:
                return None
        mid = start + (end-start) // 2
        left = self.recursive(start, mid, nums)
        right = self.recursive(mid+1, end, nums)
        if left is not None:
            return left
        if right is not None:
            return right
        return None
        

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        if len(nums)==1:
            return 0
        
        return self.recursive(0, len(nums)-1, nums)

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,1]
    assert s.findPeakElement(nums) == 2
    nums = [1,2,1,3,5,6,4]
    assert s.findPeakElement(nums) == 1 or s.findPeakElement(nums) == 5
    nums = [1,2]
    assert s.findPeakElement(nums) == 1