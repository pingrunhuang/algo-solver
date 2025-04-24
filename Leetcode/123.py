from collections import defaultdict

class Solution(object):
    MAX_TRANSACTION = 2
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        DP transition formular: 
        dp[k, i] = max(dp[k-1, i], prices[i] - prices[j] + dp[k-1, j-1]) 
        st. j < i
        i denotes i th day
        k denotes the k th transaction
        """
        if len(prices) == 0:
            return 0
        i = 1
        k = 1
        dp = defaultdict(dict)
        days = len(prices)
        for d in range(days):
            dp[0][d] = 0

        for k in range(1, Solution.MAX_TRANSACTION+1):
            dp[k][0] = 0
            for i in range(1, days):
                cost = prices[0]
                for j in range(1, i):
                    cost = min(cost, prices[j] - dp[k-1][j-1])
                dp[k][i] = max(dp[k-1][i], prices[i] - cost)
        print(dp)
        return dp[Solution.MAX_TRANSACTION][days-1]


if __name__ == "__main__":
    s = Solution()
    t = [3,3,5,0,0,3,1,4]
    assert s.maxProfit(t) == 6
    t = [1,2,3,4,5]
    assert s.maxProfit(t) == 4
    t = [7,6,4,3,1]
    assert s.maxProfit(t) == 0
