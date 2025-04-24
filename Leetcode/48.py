'''
旋转的本质：
上下颠倒 -> 对称交换

@TODO: think about counter clockwise
'''

class Solution:
    def swap(self, matrix, i,j, m,n):
        temp = matrix[i][j]
        matrix[i][j] = matrix[m][n]
        matrix[m][n] = temp

    def reverse(self, matrix, n):
        for i in range(n//2):
            temp = matrix[i]
            matrix[i] = matrix[n-i-1]
            matrix[n-i-1] = temp

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        self.reverse(matrix, n)
        for i in range(n):
            for j in range(i, n):
                self.swap(matrix, i, j, j, i)



if __name__ == '__main__':
    s = Solution()
    t1 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    s.rotate(t1)
    print(t1)