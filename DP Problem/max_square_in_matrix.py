"""
Given a n*m matrix which contains 1 and 0, find the maximum length of square of 1s in the matrix. 
Example:
0,1,1,0,1
1,1,1,1,0
1,1,1,0,0
1,1,0,0,0
1,1,0,0,0

dp:
0,1,1,0,1
1,1,2,1,0
1,2,2,0,0
1,2,0,0,0
1,2,0,0,0
The maximum length of square of 1s is 2.
"""

def max_height_square(matrix: list[list[int]]) -> int:
    n = len(matrix)
    m = len(matrix[0])
    dp = [[0 for _ in range(m)] for _ in range(n)] # dp[i][j] is the maximum height of square of 1s ending at (i,j)
    max_height = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_height = max(max_height, dp[i][j])
    return max_height

if __name__ == '__main__':
    matrix = [[0,1,1,0,1],[1,1,1,1,0],[1,1,1,0,0],[1,1,1,0,0],[1,1,0,0,0]]
    print(max_height_square(matrix))