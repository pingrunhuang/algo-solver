'''
Given an array of penny size and an aim target to be changed, calculate the number of ways changement
If that amount of money cannot be made up by any combination of the coins, return -1.

Summary:
From this solution, we can see that the recursion method actually apply to the situation where only 2 possibilities for each step
Like the fibanacci.
'''

from typing import List

class Leetcode318():
    
    def helper(self, a, b):
        if a is None and b is None:
            return None
        if a is None:
            return b
        if b is None:
            return a
        return min(a,b)
    def _coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0:0}
        for i in range(amount+1):
            print(i)
            for coin in coins:
                sub_amount = i - coin
                if sub_amount < 0:
                    continue
                if sub_amount in dp:
                    dp[i] = self.helper(dp.get(i), dp[sub_amount]+1)
        return dp.get(amount)
    def coinChange(self, coins: List[int], amount: int) -> int:
        solution = self._coinChange(coins, amount)
        return -1 if solution is None else solution
        


'''
518. Coin Change 2

You are given coins of different denominations and a total amount of money. 
Write a function to compute the number of combinations that make up that amount. 
You may assume that you have infinite number of each kind of coin.

Note: You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer
'''

class Leetcode518(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp=[0 for _ in range(amount+1)]
        dp[0]=1
        for coin in coins:
            for sub_amount in range(1, amount+1):
                if sub_amount>=coin:
                    dp[sub_amount]+=dp[sub_amount-coin]
        return dp[amount]
    def run(self):
        t1 = [1,2,5]
        # 5=5
        # 5=2+2+1
        # 5=2+1+1+1
        # 5=1+1+1+1+1
        assert self.change(5, t1) == 4


