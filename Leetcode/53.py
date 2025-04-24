'''
53. Maximum Subarray    

find the contiguous subarray with maximum sum

@TODO link to No.152
'''

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        cur_sum=nums[0]
        global_max_sum=cur_sum
        for num in nums[1:]:
            if cur_sum<0:
                cur_sum=num
            else:
                cur_sum+=num
            global_max_sum=max(cur_sum, global_max_sum)
            print(num, global_max_sum, cur_sum)
        return global_max_sum
    
    def divideAndConquer(self, nums, left, right):
        pass

        

if __name__ == "__main__":
    s = Solution()
    t1 = [-2,1,-3,4,-1,2,1,-5,4]
    assert s.maxSubArray(t1) == 6