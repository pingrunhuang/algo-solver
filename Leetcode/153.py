"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

BINARY SEARCH for O(lgN)
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                return nums[i+1]
        return nums[0]

        

if __name__ == "__main__":
    s = Solution()
    t = [3,4,5,1,2] 
    assert s.findMin(t) == 1
    t = [4,5,6,7,0,1,2]
    assert s.findMin(t) == 0