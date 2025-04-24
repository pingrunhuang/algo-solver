'''
Matrix:
Count the number of islands in a matrix
'''

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def getIsland(i,j):
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]=='1':
                grid[i][j]='0'
                return 1+getIsland(i-1,j)+getIsland(i+1,j)+getIsland(i,j+1)+getIsland(i,j-1)
            return 0
        result=0
        for row, cols in enumerate(grid):
            for col, val in enumerate(cols):
                if getIsland(row,col)>0:
                    result+=1
        return result
        

if __name__=='__main__':
    solution = Solution()
    t1=[
        [1,1,1,1,0],
        [1,1,0,1,0],
        [1,1,0,0,0],
        [0,0,0,0,0]]
    print(solution.numIslands(t1))