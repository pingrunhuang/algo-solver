"""
A rabbit can only move one grid from left to right, or from up to down, given a n by m maze, how many ways can the rabbit move from top left to down right?
"""

def solve_maze_problems(n,m):
    """
    Transition equation: 
    solve_maze_problems(i,j)=solve_maze_problems(i,j-1)+solve_maze_problems(i-1,j)
    definition of dp: dp[i][j] means how many ways can the rabbit come to this grid from maze[0][0]
    """
    dp = [[0]*(m) for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1
    for j in range(m):
        dp[0][j]=1
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp)
    return dp[-1][-1]

if __name__ == "__main__":
    print(solve_maze_problems(6, 18))