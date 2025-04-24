class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        - Integers in each row are sorted from left to right.
        - The first integer of each row is greater than the last integer of the previous row.
        """
        ROWS = len(matrix)
        if ROWS==0:
            return False
        COLS = len(matrix[0])
        if COLS==0:
            return False
        i = 0 
        while i < ROWS:
            if matrix[i][0]<target:
                i+=1
            elif target==matrix[i][0]:
                return True
            else:
                break
        if target in matrix[i-1]:
            return True
        return False

        

if __name__ == "__main__":
    s = Solution()
    matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    assert s.searchMatrix(matrix, 13)==False
    assert s.searchMatrix(matrix, 3)==True
    assert s.searchMatrix([], 3)==False
    assert s.searchMatrix([[1]], 2)==False