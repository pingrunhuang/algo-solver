'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
'''
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        up_bound = 0
        low_bound = len(matrix)-1
        left_bound = 0
        right_bound = len(matrix[0])-1
        result = []
        n=len(matrix[0])*len(matrix)
        # note the condition here, I use != before which did not pass
        while left_bound <= right_bound and up_bound <= low_bound:
            # print(left_bound,right_bound, up_bound, low_bound, i, j)
            for j in range(left_bound, right_bound+1):
                result.append(matrix[up_bound][j])
            up_bound+=1
            for i in range(up_bound, low_bound+1):
                result.append(matrix[i][right_bound])
            right_bound-=1
            for j in range(right_bound, left_bound-1, -1):
                result.append(matrix[low_bound][j])
            low_bound-=1
            for i in range(low_bound, up_bound-1, -1):
                result.append(matrix[i][left_bound])
            left_bound+=1
        #print(result[:n])
        # note here to subtract the result to only keep the required length of element, in case some duplicate element included
        return result[:n]

    def spiralOrder2(self, matrix):
        """in a rotate manner
            |1 2 3|      |6 9|      |8 7|      |4|  =>  |5|  =>  ||
            |4 5 6|  =>  |5 8|  =>  |5 4|  =>  |5|
            |7 8 9|      |4 7|
        """
        # a and b means if one of a and b is None or false, return the first one, else return the latter one
        # * means unpack the zip object
        return matrix and [*matrix.pop(0)] + self.spiralOrder2([*zip(*matrix)][::-1])


if __name__ == "__main__":
    s = Solution()
    t1 = [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]
    print(s.spiralOrder2(t1))
    t2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]
    ]
    print(s.spiralOrder2(t2))
    t3 = [[1,2],[3,4]]
    print(s.spiralOrder2(t3))