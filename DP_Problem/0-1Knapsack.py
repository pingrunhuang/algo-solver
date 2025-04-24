'''
Given a total weight one can carry, determine the maximum value one can have

This is the comparison of the efficiency
recursion: 5.125999450683594e-05
dp: 1.7881393432617188e-05
5 times faster

Conclusion:
Always try to record some repeated middle result! 
'''
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


class Solution:
    def __init__(self, ws, vs):
        assert type(ws)==list
        assert type(vs)==list
        self.items = [
            Item(w, v) for w in ws for v in vs
        ]
        # a matrix to a given item index and the current capacity, the total value we could get
        self.dp = [
            {} for _ in ws
        ]

    def Knapsack_rec(self, cur_item_index, cur_capacity):
        if cur_item_index== 0 or cur_capacity==0:
            return 0
        
        if self.items[cur_item_index].weight > cur_capacity:
            return self.Knapsack_rec(cur_item_index-1, cur_capacity)
        else:
            yes_choise = self.items[cur_item_index].value + self.Knapsack_rec(cur_item_index-1, cur_capacity-self.items[cur_item_index].weight)
            no_choise = self.Knapsack_rec(cur_item_index-1, cur_capacity)
            return max(yes_choise, no_choise)

    def Knapsack_dp(self, cur_item_index, cur_capacity):
        """
        With the previous recursion solution, we found that given a current capacity and the index of the item, we could record it for later use.
        """
        if self.dp[cur_item_index].get(cur_capacity):
            return self.dp[cur_item_index].get(cur_capacity)
        
        if cur_item_index==0 or cur_capacity==0:
            return 0

        else:
            yes_choise = self.items[cur_item_index].value + self.Knapsack_dp(cur_item_index-1, cur_capacity-self.items[cur_item_index].weight)
            no_choise = self.Knapsack_dp(cur_item_index-1, cur_capacity)
            self.dp[cur_item_index][cur_capacity]=max(yes_choise, no_choise)
            return max(yes_choise, no_choise)

if __name__=='__main__':
    import time
    w1 = [1,2,4,2,5]
    v1 = [5,3,5,3,2]
    s = Solution(w1, v1)
    start = time.time()
    print(s.Knapsack_rec(4,10))
    print(time.time() - start)
    start = time.time()
    print(s.Knapsack_dp(4, 10))
    print(time.time()-start)