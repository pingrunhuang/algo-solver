"""
House robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

DP FIBONACCI
DP solution
"""
class Solution(object):
    def rob(self, nums):
        """
        O(1) memory space
        O(n) time space
        :type nums: List[int]
        :rtype: int
        """
        prev_rob = 0
        max_rob = 0
        for i in range(len(nums)):
            temp_rob = max(max_rob, nums[i]+prev_rob)
            prev_rob, max_rob = max_rob, max(max_rob, temp_rob)
        return max_rob


class Solution2(object):
    def rob(self, nums):
        """
        O(n) memory space
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        self.memo = {0: nums[0], -1:0}
        for i in range(1, n):
            self.memo[i] = max(nums[i] + self.memo[i-2], self.memo[i-1])
        return self.memo[n-1]

class Solution3:
    def rob(self, nums) -> int:
        if len(nums)==1:
            return nums[0]
        
        cum_money = [0 for _ in range(len(nums))]
        cum_money[0] = nums[0]
        cum_money[1] = max(nums[0], nums[1])
        i = 2
        while i < len(nums):
            cum_money[i] = max(cum_money[i-1], nums[i]+cum_money[i-2])
            i+=1

        return cum_money[-1]
            

if __name__ == "__main__":
    solution = Solution2()
    t = [2,7,9,3,1]
    print(solution.rob(t))
    t = [1,2]
    print(solution.rob(t))
    t = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    print(solution.rob(t))