'''
Toeplitz Matrix

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
 

Example 1:

Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: True
Explanation:
1234
5123
9512

In the above grid, the diagonals are "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]", and in each diagonal all elements are the same, so the answer is True.
Example 2:

Input: matrix = [[1,2],[2,2]]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.
Note:

matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].

'''

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        isMatch={}
        # suppose p(x1,y1) and p(x2,y2) are in the same diagnose, then x1-x2==y1-y2
        for r in range(rows):
            for c in range(cols):
                if isMatch.get(c-r, -1)!=-1:
                    if matrix[r][c]!=isMatch.get(c-r):
                        return False
                else:
                    isMatch[c-r]=matrix[r][c]
        return True
    
    def isToeplitzMatrix2(self, matrix):
        return all(r==0 or c==0 or matrix[r-1][c-1]==matrix[r][c] for r, row in enumerate(matrix) for c, v in enumerate(row))

if __name__=='__main__':
    solution=Solution()
    testCase1=[[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    print(solution.isToeplitzMatrix(testCase1))
    testCase2=[[1,2],[2,2]]
    print(solution.isToeplitzMatrix(testCase2))
    testCase3=[[18],[66]]
    print(solution.isToeplitzMatrix(testCase3))
    testCase4=[[0,33,98],[34,22,33]]
    print(solution.isToeplitzMatrix(testCase4))

    print("Plan B:")
    print(solution.isToeplitzMatrix2(testCase1))
    print(solution.isToeplitzMatrix2(testCase2))
    print(solution.isToeplitzMatrix2(testCase3))
    print(solution.isToeplitzMatrix2(testCase4))