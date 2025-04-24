"""
154. Find Minimum in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Would allow duplicates affect the run-time complexity? How and why?
    Not really for the O(n) solution
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        


if __name__ == "__main__":
    s = Solution()
    t = [2,2,2,0,1]
    assert s.findMin(t) == 0
    t = [1,3,5]
    assert s.findMin(t) == 1