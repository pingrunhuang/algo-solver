class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return []
        if rowIndex == 1:
            return [1]
        if rowIndex == 2:
            return [1,1]
        result = [None for _ in range(rowIndex)]
        if rowIndex%2==0:
            for i in range(rowIndex//2):
                result[i] = i*i+1
            for i in range(rowIndex//2, rowIndex):
                result[i] = result[rowIndex-i-1]
            return result
        if rowIndex%2!=0:
            for i in range(rowIndex//2+1):
                result[i] = i*i+1
            for i in range(rowIndex//2+1, rowIndex):
                result[i] = result[rowIndex-i-1]
            return result

class Solution2(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        if rowIndex == 2:
            return [1,2,1]
        lastRow = self.getRow(rowIndex-1)
        result = [1]
        for i in range(1, rowIndex):
            result.append(lastRow[i-1]+lastRow[i])
        result.append(1)
        return result
    
if __name__ == "__main__":
    s = Solution2()
    print(s.getRow(3))