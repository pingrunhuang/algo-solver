'''
807. Max Increase to Keep City Skyline

'''

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        result = 0
        row_max = []
        col_max = []
        for row in range(n):
            row_max.append(max(grid[row]))
            col_max.append(max(  grid[col][row] for col in range(n) ) )

        
        for row in range(n):
            for col in range(n):
                result += min(row_max[row], col_max[col]) - grid[row][col]
        return result


if __name__ == "__main__":
    solution = Solution()
    t1 = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
    print(solution.maxIncreaseKeepingSkyline(t1))
