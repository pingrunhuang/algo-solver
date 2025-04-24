"""
168. Excel Sheet Column Title

chr(97) == a
chr(65) == A
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""
        while n>0:
            # why (n-1)???: think about the corner case of 26, 52, ... 
            result = chr(ord('A') + (n-1)%26) + result
            n = (n-1)//26
        return result

class Solution2(object):
    def convertToTitle(self, n):
        return "" if n == 0 else self.convertToTitle((n - 1) // 26) + chr((n - 1) % 26 + ord('A'))


if __name__ == "__main__":
    s = Solution()
    t = 1 
    s.convertToTitle(t)
    t = 28
    s.convertToTitle(t)
    t = 701
    s.convertToTitle(t)
    t = 24568
    s.convertToTitle(t)
    t = 52
    s.convertToTitle(t)