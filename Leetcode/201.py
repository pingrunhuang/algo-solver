class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        TODO: RuntimeError
        :type m: int
        :type n: int
        :rtype: int
        """
        if n == m:
            return n
        if m == 0:
            return m

        res = m
        for x in range(m, n):
            print(x)
            res &= x
        
        return res & n
        
    
if __name__ == "__main__":
    m = 1
    n = 2147483647
    s = Solution()
    print(s.rangeBitwiseAnd(m, n))