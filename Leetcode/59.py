'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Opposite way from No. 54
'''

class Solution:
    def inside_out(self, n):
        '''
        ||  =>  |9| =>  |8|      |6 7|      |4 5|      |1 2 3|
                        |9|  =>  |9 8|  =>  |9 6|  =>  |8 9 4|
                                            |8 7|      |7 6 5|
        [range(10, 10)]
        [range(9, 10)]
        [range(8, 9), (9,)]
        [range(6, 8), (9, 8)]
        [range(4, 6), (9, 6), (8, 7)]
        [range(1, 4), (8, 9, 4), (7, 6, 5)]
        '''
        result = []
        low = n*n+1
        while low > 1:
            low , high = low - len(result), low 
            result = [range(low, high)] + [*zip(*result[::-1])]
            # print(result)
        return list(map(lambda x:[*x], result))
    def walk_spiral(self, n):
        result = [[0 for _ in range(n)] for _ in range(n)]
        i, j, directioni, directionj = 0,0,0,1
        for x in range(n*n):
            result[i][j]=x+1
            if result[(i+directioni)%n][(j+directionj)%n]:
                directioni, directionj = directionj, - directioni
            i+=directioni
            j+=directionj
        return result


    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # return self.inside_out(n)
        return self.walk_spiral(n)
        
        

if __name__ == "__main__":
    s = Solution()
    t1 = 3
    print(s.generateMatrix(t1))
    t1 = [
        [ 1, 2, 3 ],
        [ 8, 9, 4 ],
        [ 7, 6, 5 ]
        ]
