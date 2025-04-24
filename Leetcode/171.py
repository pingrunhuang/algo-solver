"""
171. Excel Sheet Column Number


related: 168 
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1
        result = 0
        for x in s:
            result += (ord(x) - ord('A')+1)*(26**i)
            i -= 1
        return result

if __name__ == "__main__":
    s = Solution()
    Input = "A"
    Output = 1
    assert s.titleToNumber(Input) == Output

    Input = "AB"
    Output = 28
    assert s.titleToNumber(Input) == Output

    Input = "ZY"
    Output = 701
    assert s.titleToNumber(Input) == Output