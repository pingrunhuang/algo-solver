'''
518. Coin Change 2

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

Note: You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer
'''

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """

        dp=[0 for _ in range(amount+1)]
        dp[0]=1
        # 思考为什么先遍历coin再是amount
        # dp 在这里表示要凑够某个amount，需要给定m个coin可以有的最多组合，m<=len(coins)
        for coin in coins:
            for sub_amount in range(1, amount+1):
                if sub_amount>=coin:
                    dp[sub_amount]+=dp[sub_amount-coin]
        return dp[amount]
        

if __name__ == "__main__":
    s = Solution()
    t1 = [1,2,5]
    # 5=5
    # 5=2+2+1
    # 5=2+1+1+1
    # 5=1+1+1+1+1
    assert s.change(5, t1) == 4