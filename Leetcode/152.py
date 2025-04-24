"""
152. Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array 
(containing at least one number) which has the largest product.

TODO: corner case 
link to No.53
"""

import sys
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MIN = nums[0]
        MAX = nums[0]
        RES = nums[0]
        for i in range(1, len(nums)):
            # all depends on current number is larger then 0 or not
            if nums[i]>0:
                MAX = max([nums[i], MAX * nums[i]])
                MIN = min([nums[i], MIN * nums[i]])
            else:
                last_max = MAX
                MAX = max([nums[i], MIN * nums[i]])
                MIN = min([nums[i], last_max * nums[i]])
            RES = max([MAX, RES])
        return RES

        # start_index = 0
        # end_index = 0
        # num_size = len(nums)
        # result = - sys.maxsize
        # temp_result = nums[0]
        # while end_index<num_size:
        #     if start_index == end_index:
        #         temp_result = nums[end_index]
        #     else:
        #         temp_result = nums[end_index]*temp_result
        #     end_index+=1

        #     if temp_result>result:
        #         result = temp_result
        #     else:
        #         start_index = end_index
        #     print('start, end', start_index, end_index)
        # return result



if __name__ == "__main__":
    s = Solution()
    t = [2,3,-2,4]
    assert s.maxProduct(t) == 6
    t = [-2,0,-1]
    assert s.maxProduct(t) == 0
    t = [0,2]
    assert s.maxProduct(t) == 2