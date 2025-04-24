
'''
Here is the solution come from the leetcode explanation which remind me of upgrade the dimensionality. 


In a N x N grid representing a field of cherries, each cell is one of three possible integers.

0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and pass through;
-1 means the cell contains a thorn that blocks your way.
Your task is to collect maximum number of cherries possible by following the rules below:

Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1);
After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.

'''
'''
Conditions:
    1. col = cur_steps - row
    2. reward[row, col] = max(reward[row+1][col]-grid[row+1][col], reward[row][col+1]-grid[row][col+1])
    3. reward[0,0]=0


'''
# TODO
class Solution(object):

    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        # how to define negative infinitive in python
        # float('inf') for infinitive
        NINF = float('-inf')
        # note here how to write fast check statement nested inside a generator!!!!
        # accumulated_reward = [[x if x!=-1 else NINF for x in y] for y in grid]
        # for e in accumulated_reward:
        #     e.append(NINF)

        row1 = 0
        col1 = 0
        row2 = 0
        col2 = row1+col1-row2

        accumulated_reward = [[0 for _ in x] for x in grid]
        for row in range(N)-1:
            for col in grid[row]:
                if row == col:

        

if __name__ == '__main__':
    test_case1 = [
        [1,1,-1],
        [1,0,-1],
        [1,1,1]
    ]
    solution = Solution()
    r1 = solution.cherryPickup(test_case1)

    test_case2 = [
        [1,1,1,0,0],
        [0,0,1,0,1],
        [1,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,1,1]
    ]
    r2 = solution.cherryPickup(test_case2)
    print("Result1:", r1, "\nResult2:", r2, "\n")

    