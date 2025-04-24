"""
Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


The basic assumption here is that the more transaction you have, the invester should get more benifit out of it.

i: number of transaction at the moment
j: current day
m: 0 to j-1

The equation here means: we either do transaction on day j so that our asset is summary of today's transaction benifit and the previous days where I have 1 less transation
or 
we do nothing today.
Either case, we should keep the max benifit after such operation 
asset[i][j] = max(max([asset[i-1][m] - prices[m] + prices[j] for m in range(0, j)]), asset[i][j-1]) 

max([asset[i-1][m] - prices[m] + prices[j] for m in range(0, j)]) this part can also be stored as a variable

Notice in this situation, we can sell and immediately buy on the same day
"""

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        days = len(prices)
        if days <= 1 or k == 0:
            return 0
        if  k >= days // 2:
            return sum([i-j for i, j in zip(prices[1:], prices[:-1]) if i-j>0])
                        
        asset_table = [[0] * days for _ in range(k+1)]
        for i in range(1, k+1):
            local_max = [0] * days
            for j in range(1, days):
                today_profit = prices[j] - prices[j-1]

                local_max[j] = max(
                    # We have made profit in (j - 1) days.
                    # We want to cancel the day (j - 1) sale and sell it on day j.
                    local_max[j-1] + today_profit,
                    # We have made max profit with (i - 1) transations in (j - 1) days.
                    # For the last transation, we buy stock on day (j - 1) and sell it on day j.
                    asset_table[i-1][j-1] + today_profit,
                    # do nothing on day j
                    asset_table[i-1][j-1]
                )

                asset_table[i][j] = max(local_max[j], asset_table[i][j-1])
        
        return asset_table[k][-1]


class Solution2(object):
    """
    https://www.youtube.com/watch?v=Pw6lrYANjz4

    time: O(n*k)
    space: O(n)
    """
    def maxProfit(self, k, prices):
        days = len(prices)
        if days <= 1 or k == 0:
            return 0
        if  k >= days // 2:
            return sum([i-j for i, j in zip(prices[1:], prices[:-1]) if i-j>0])
        
        asset_table = [[0] * days for _ in range(k+1)]
        for i in range(1, k+1):
            asset_after_buy = asset_table[i-1][0] - prices[0]
            
            for j in range(1, days):
                if asset_table[i-1][j-1] - prices[j-1] > asset_after_buy:
                    asset_after_buy = asset_table[i-1][j-1] - prices[j-1]
                asset_table[i][j] = max(asset_after_buy + prices[j], asset_table[i][j-1])

        return asset_table[k][-1]


if __name__ == "__main__":
    solution = Solution2()
    t = ([2,4,1], 2)
    assert solution.maxProfit(t[1], t[0]) == 2
    t = ([3,2,6,5,0,3], 2)
    assert solution.maxProfit(t[1], t[0]) == 7
    t = ([1,2,4,2,5,7,2,4,9,0], 2)
    assert solution.maxProfit(t[1], t[0]) == 13