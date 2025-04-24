"""
This time can complete multiple transactions as many as you can.
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Thoughts: same like the question 121, but when there is a fall, we will sale it and switch the buying day to that fall
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buying_index = 0
        current_index = 1
        # used to describe the trend of the stock
        previous_index = 0
        days = len(prices)
        max_profit = 0
        while current_index < days:
            # if the stock keep raising till the end, buy and sale on the last day
            if prices[current_index] >= prices[previous_index] and current_index==days-1:
                max_profit += prices[current_index] - prices[buying_index]
            # once there is a fall on the price, sale the stock which means buying on the local lowest day(the fall) and set the previous index to current index
            elif prices[current_index] < prices[previous_index]:
                max_profit += prices[previous_index] - prices[buying_index]
                buying_index = current_index
                previous_index = current_index
            elif prices[current_index] > prices[previous_index]:
                previous_index = current_index
            current_index += 1
        return max_profit

if __name__ == "__main__":
    s = Solution()
    test1 = [7,1,5,3,6,4]
    test2 = [1,2,3,4,5]
    test3 = [7,6,4,3,1]
    test4 = [1,9,6,9,1,7,1,1,5,9,9,9]
    print(s.maxProfit(test1))
    print(s.maxProfit(test2))
    print(s.maxProfit(test3))
    print(s.maxProfit(test4)) # 25
