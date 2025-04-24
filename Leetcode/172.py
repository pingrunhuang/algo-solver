"""
172. Factorial Trailing Zeroes
Given an integer n, return the number of trailing zeroes in n!.

Explanation
the number of zeros is the minimum of the number of 2 and the number of 5.

Since multiple of 2 is more than multiple of 5, the number of zeros is dominant by the number of 5.
"""

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        result = 0
        while 5**i<=n:
            result += n // 5**i
            i+=1
        return result
        
if __name__ == "__main__":
    s = Solution()
    t = 5
    assert s.trailingZeroes(t) == 1
    t = 2147483647


