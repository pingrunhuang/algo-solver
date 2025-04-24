"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
TODO
"""

class Solution:

  def uniquePaths(self, m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    grid = Grid(m, n)
    self.result = 0
    def dfs(current_x, current_y):
      if n-1 == current_y and m-1 == current_x:
        self.result+=1
        print("reached!!!!")
        return
      else:
        if current_x < m-1 and current_y < n-1:
          print("Going right")
          grid.update(current_x, current_y)
          grid.show()
          dfs(current_x+1, current_y)
          print()
          print("Going down")
          grid.update(current_x, current_y)
          grid.show()
          dfs(current_x, current_y+1)
          return
        elif current_x <= m-1 and current_y == n-1:
          print("Right")
          grid.update(current_x, current_y)
          grid.show()
          dfs(current_x+1, current_y)
          return 
        elif current_y <= n-1 and current_x == m-1:
          print("Down")
          grid.update(current_x, current_y)
          grid.show()
          dfs(current_x, current_y+1)
          return
  
    dfs(0,0)
    print(self.result)
    return self.result


class Grid:
  def __init__(self, cols, rows):
    self.cols = cols
    self.rows = rows
  
  def update(self, current_x, current_y):
    self.matrix = [["*" if j == current_x and i == current_y  else "O" for j in range(self.cols)] for i in range(self.rows) ]
  
  def show(self):
    for row in range(self.rows):
      print("-"*self.cols*2)
      print("|".join(self.matrix[row]))  
  



if __name__ == "__main__":
  s =  Solution()
  # assert s.uniquePaths(3, 2) == 3
  # assert s.uniquePaths(7, 3) == 28
  assert s.uniquePaths(23, 12) == 12