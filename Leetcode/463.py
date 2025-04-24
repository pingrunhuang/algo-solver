'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. 
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, 
and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). 
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.


TIPS:
TOTAL - duplicated

Matrix
'''

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        pieces, neighbours=0, 0
        for row , cols in enumerate(grid):
            for col, val in enumerate(cols):
                if val==1:
                    pieces+=1
                    if row<len(grid)-1 and grid[row+1][col]==1:
                        neighbours+=1
                    if col<len(grid[0])-1 and grid[row][col+1]==1:
                        neighbours+=1
        return 4*pieces-2*neighbours
        

if __name__=='__main__':
    testcase1=[
        [0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]
    solution = Solution()
    print(solution.islandPerimeter(testcase1))
