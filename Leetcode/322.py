'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.


Solution:

coinChange(11) = min{coinChange(11-5), coinChange(11-2), coinChange(11-1)}+1
TIME LIMIT EXCEED!
'''
import time

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # initialization
        dp      = {0:0}
        MAX     = amount+1
        # transform equation: dp[i]=min{dp[i], min{dp[i-coins[0]],..., dp[i-coins[j]]}+1}
        coins.sort()
        for sub_amount in range(1, amount+1):
            for coin in coins:
                if coin<=sub_amount:
                    dp[sub_amount] = min(dp.get(sub_amount-coin, MAX)+1, dp.get(sub_amount, MAX))
                else:
                    break
        print(dp)
        return dp.get(amount, MAX) if dp.get(amount, MAX)<=amount else -1 

if __name__ == "__main__":
    import pytest
    s = Solution()
    t1 = [1,2,5]
    assert s.coinChange(t1, 11) == 3
    t2 = [2]
    assert s.coinChange(t2, 3) == -1
    t3 = [146,66,355,93,255,152,225,244,168,205]
    start = time.time()
    s.coinChange(t3, 8069)
    print(time.time()-start)
    t4 = [2]
    assert s.coinChange(t4, 1) == -1