
'''
BFS

Matrix
'''

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area=0
        temp_max_area=0
        def area(i,j):
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]==1:
                grid[i][j]=0
                return 1 + area(i+1,j)+area(i-1,j)+area(i,j+1)+area(i,j-1)
            return 0
        for row, cols in enumerate(grid):
            for col, val in enumerate(cols):
                temp_max_area=area(row, col)
                if max_area<temp_max_area:
                    max_area=temp_max_area
                    temp_max_area=0
        return max_area
                    

if __name__=='__main__':
    testCase1=[
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    testCase2=[[0,0,0,0,0,0,0,0]]
    testCase3=[[1]]
    solution = Solution()
    print(solution.maxAreaOfIsland(testCase1))
    print(solution.maxAreaOfIsland(testCase2))
    print(solution.maxAreaOfIsland(testCase3))
