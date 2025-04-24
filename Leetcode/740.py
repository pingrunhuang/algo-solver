from typing import List

"""
delete and earn

a transformation of the house robber

dp solution
"""

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        nums.sort()

        prev_points = 0
        max_points = 0
        i = 0
        while i < len(nums):
            j = self.findNext(nums, i)
            cur_points = self.calcPoints(nums, i, j)
            print(prev_points)
            temp = max(max_points, prev_points+cur_points)
            if j<len(nums) and nums[j]==nums[i]+1:
                prev_points = max_points
            else:
                prev_points = temp

            print(i,j,temp,max_points, prev_points)
            max_points = temp
            i=j
            
        return max_points

    def findNext(self, nums, i):
        cur_val = nums[i]
        while i<len(nums) and nums[i]==cur_val:
            i+=1
        return i
    
    def calcPoints(self, nums, i, j):
        return (j-i)*nums[i]