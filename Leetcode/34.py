'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

required
related: binary search 
'''
from utils import assertion_print

class Solution:
    def search_left_most_index(self, nums, left, right, target, index:int=-1):
        while left <= right:
            mid = (left+right)//2
            if nums[mid]==target:
                right = mid-1
                index = self.search_left_most_index(nums, left, right, target, mid)
            elif nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
        return index

    def search_right_most_index(self, nums, left, right, target, index:int=-1):
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                left=mid+1
                index=self.search_right_most_index(nums, left, right, target, mid)
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return index

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)==0:
            return [-1,-1]
        if len(nums)==1:
            if nums[0]==target:
                return [0,0]
            else:
                return [-1,-1]
        l = 0
        r = len(nums)-1
        lowest_idx = self.search_left_most_index(nums, l, r, target)
        highest_idx = self.search_right_most_index(nums, l, r, target)
        return [lowest_idx, highest_idx]

    def run(self):
        nums = [5,7,7,8,8,10]
        assertion_print(self.searchRange(nums, 8), [3,4])
        assertion_print(self.searchRange(nums, 6), [-1,-1])
        nums = [2,2]
        assertion_print(self.searchRange(nums, 2),[0,1])
        nums = [1,4]
        assertion_print(self.searchRange(nums, 4), [1,1])
        nums=[1,2,5,5,5,9]
        assertion_print(self.searchRange(nums, 5), [2,4])
        nums = [0,0,0,1,2,3]
        assertion_print(self.searchRange(nums, 0), [0,2])
    

if __name__ == "__main__":
    s = Solution()
