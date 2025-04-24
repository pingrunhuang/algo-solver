"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1], [1,1]]
        result = [[1],[1,1]]
        for row in range(3,numRows+1):
            new_row = []
            for col in range(row):
                if col==0:
                    new_row.append(1)
                elif col==row-1:
                    new_row.append(1)
                else:
                    new_row.append(result[row-2][col-1]+result[row-2][col])
            result.append(new_row)
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.generate(1))