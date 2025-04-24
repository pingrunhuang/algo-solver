"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
"""
from typing import List

class Solution1:
    """
    brute force solution which will cause time limit error
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0 
        for i in range(n):
            for j in range(i, n):
                if sum(nums[i:j+1])==k:
                    count+=1
        return count
    

class Solution2:
    """
    an optimized solution which will use sum(i,j)=sum(0,j)-sum(0,i) property and store in memory
    the idea is to form a sum to k, we can record the previous sum in dictionary
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        memory = {0:1}
        prefix_sum = 0
        count = 0
        for num in nums:
            prefix_sum += num
            residual = k - num # used to check if nums[:j] - nums[:i] = nums[i:j] == k
            if residual in memory: # meaning this num match the requirement
                count += memory[residual]
            
            if prefix_sum in memory:
                memory[prefix_sum]+=1
            else:
                memory[prefix_sum]=1
        return count
    

if __name__=="__main__":
    t = [1,2,1,2,1]
    s = Solution2()
    print(s.subarraySum(t, 3))