'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
'''
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        O(m+n) space, O(m*n) time 
        """
        rows = set()
        cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    rows.add(i)
                    cols.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j]=0


class Solution2:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        O(1) space
        """
        if len(matrix)==1:
            if 0 in matrix[0]:
                for j in range(len(matrix[0])):
                    matrix[0][j]=0

        elif len(matrix[0])==1:
            if [0] in matrix:
                for i in range(len(matrix)):
                    matrix[i][0]=0

        else:
            # preset the column for later check if the first column need to be set
            is_set_first_col = False
            is_set_first_row = False
            for j in range(len(matrix[0])):
                if matrix[0][j]==0:is_set_first_row=True
            # mark 
            for i in range(len(matrix)):
                if matrix[i][0]==0:is_set_first_col=True
                # notice I left out the first column here for later 
                for j in range(1, len(matrix[0])):
                    if matrix[i][j]==0:
                        matrix[i][0]=0
                        matrix[0][j]=0

            # leave out the edge case
            for i in range(1, len(matrix)):
                for j in range(1, len(matrix[0])): 
                    if matrix[i][0]==0 or matrix[0][j]==0:
                        matrix[i][j]=0
            # handle the edge case
            # see if I need to change the first row
            if is_set_first_row:
                for j in range(len(matrix[0])):
                    matrix[0][j]=0
            # see if I need to change the first col
            if is_set_first_col:
                for i in range(len(matrix)):
                    matrix[i][0]=0


if __name__ == '__main__':
    s = Solution2()
    t1 = [
        [1,1,1],
        [1,0,1],
        [1,1,1]
    ]
    s.setZeroes(t1)
    print(t1)

    t2 = [
        [0,1,2,0],
        [3,4,5,2],
        [1,3,1,5]
    ]
    s.setZeroes(t2)
    print(t2)
    t3 = [
        [1,1,1],
        [0,1,1],
        [1,1,1]
    ]
    s.setZeroes(t3)
    print(t3)