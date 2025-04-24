"""
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Thoughts:
1. Initial thought is to traverse the price list 2 times with time complexity O(n^2)
2. Do better? Better solution is use 2 pointers to keep track of the current_buying and current_saling index respectively
"""

class Solution:
    """
    of course, we ran out of time limit    
    """
    def maxProfit(self, prices) -> int:
        max_profit = 0
        for buying_day, buying_price in enumerate(prices):
            for saling_price in prices[buying_day+1:]:
                if saling_price-buying_price>max_profit:
                    max_profit = saling_price-buying_price
        return max_profit

class Solution2:
    def maxProfit(self, prices):
        buying_index = 0
        current_index = 1
        days = len(prices)
        max_profit = 0
        while current_index < days:
            if prices[current_index] - prices[buying_index]>max_profit:
                max_profit = prices[current_index] - prices[buying_index]
            elif prices[current_index]<prices[buying_index]:
                buying_index = current_index
            current_index += 1
        return max_profit


if __name__ == "__main__":
    s = Solution2()
    test1 = [7,1,5,3,6,4]
    test2 = [7,6,4,3,1]
    print(s.maxProfit(test1))
    print(s.maxProfit(test2))
