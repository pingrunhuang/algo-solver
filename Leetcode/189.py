"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
"""
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            last = nums.pop()
            nums.insert(0, last)
            k -= 1
        return nums

if __name__ == "__main__":
    s = Solution()
    t1 = ([1,2,3,4,5,6,7], 3)
    assert s.rotate(t1[0], t1[1]) == [5,6,7,1,2,3,4]
    t2 = ([-1,-100,3,99], 2)
    assert s.rotate(t2[0], t2[1]) == [3,99,-1,-100]