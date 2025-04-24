'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. 
If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

Note:
log n should remind me of bst

REDO
'''

class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        minimal_length=len(nums)+1

        start,end,temp_sum=0,0,0
        while end<len(nums):
            temp_sum+=nums[end]
            end+=1
            while temp_sum>=s:
                temp_sum-=nums[start]
                start+=1
                if minimal_length>end-start+1:
                    minimal_length=end-start+1
        if minimal_length == len(nums)+1:
            return 0
        return minimal_length


if __name__=='__main__':
    solution = Solution()
    testCase1=[2,3,1,2,4,3]
    s1 = 7
    print(solution.minSubArrayLen(s1, testCase1))