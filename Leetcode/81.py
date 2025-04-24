'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

related to: leetcode 33
'''

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums)==0:
            return False
        len_nums = len(nums)
        if nums[0]>=target:
            for i, v in enumerate(nums):
                if v==target:
                    return True
        else:
            for i in range(len_nums-1, -1, -1):
                if nums[i]==target:
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    nums = [2,5,6,0,0,1,2]
    target = 0
    assert s.search(nums, target)==True

    nums = [2,5,6,0,0,1,2]
    target = 3
    assert s.search(nums, target) == False

    nums = [1,3,1,1,1]
    target = 3
    assert s.search(nums, target) == True