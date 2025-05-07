"""
dp solution:
find the transition equation
max(nums, i) = nums[i] + max(nums, i-1)>0?max(nums, i-1):0
"""

class Leetcode53:
    def maxSubArray(self, nums: list)->int:
        n = len(nums)
        dp = [None for _ in range(n)]
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = nums[i] + (dp[i-1] if dp[i-1]>0 else 0)
        return max(dp)