'''
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, 
and you can either start from the step with index 0, or the step with index 1. 
'''

class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost)==0:
            return 0
        if len(cost)==1:
            return cost[0]
        
        if len(cost)==2:
            return min(cost[0], cost[1])
        
        f2=cost[0]
        f1=cost[1]
        for i in range(2,len(cost)):
            f0=min(f1, f2) + cost[i]
            f2=f1
            f1=f0
        return min(f1,f2)

        # return  self.minCostClimbingStairs(cost[:cur_index-1]) + cost[cur_index] \
        #     if self.minCostClimbingStairs(cost[:cur_index-1]) < self.minCostClimbingStairs(cost[:cur_index-2]) \
        #         else self.minCostClimbingStairs(cost[:cur_index-2]) + cost[cur_index]



if __name__=='__main__':
    solution = Solution()
    testCase1 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(solution.minCostClimbingStairs(testCase1))
    testCase2 = [10, 15, 20]
    print(solution.minCostClimbingStairs(testCase2))