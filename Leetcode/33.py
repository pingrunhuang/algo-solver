"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

related to 81
"""
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return -1
        len_nums = len(nums)
        if nums[0]>=target:
            for i, v in enumerate(nums):
                if v==target:
                    return i
        else:
            for i in range(len_nums-1, -1, -1):
                if nums[i]==target:
                    return i
        return -1
    def binarySearch(self, nums, target):
        if len(nums)==0:
            return -1
        l = 0
        r = len(nums)-1
        # # initailly I want to separate the list into 2 parts: target belongs to the left part
        # if target<nums[0]:
        #     while(nums[-1] < nums[l]):
        #         mid = l+(r-l)//2
        #         # avoid the situation where l is not changed
        #         if target 
        # else:
        #     while(nums[r]<nums[0]):
        #         mid = l+round((r-l)/2) 
        #         r = mid
        # print(l,r)
        while l<r:
            mid = l + (r-l)//2
            if nums[mid]==target:
                return mid

            if nums[l] <= nums[mid]:
                # devide the right part into 2 parts separated by the target value
                if target < nums[mid] and target >= nums[l]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if target > nums[mid] and target<= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return l if nums[l]==target else -1




if __name__ == "__main__":
    s = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(s.binarySearch(nums, target))
    nums = [1,3]
    target = 0
    print(s.binarySearch(nums, target))
    nums=[1]
    target=1
    print(s.binarySearch(nums,target))
    nums=[5,1,3]
    target=1
    print(s.binarySearch(nums,target))
    nums=[3,1]
    target=0
    print(s.binarySearch(nums,target))
    nums=[4,5,6,7,8,1,2,3]
    target=8
    print(s.binarySearch(nums, target))
    nums=[5,1,2,3,4]
    target=1
    print(s.binarySearch(nums, target))
