from unittest import TestCase, main

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        res = 1
        for i in range(1, n):
            # because for n>3, integerBreak(n) will break n into at least 2 parts
            # so we need to compare the 2 parts only scenario separately
            res = max(res, i*(n-i), i*self.integerBreak(n-i))
        return res

    def integerBreak_memo(self, n: int) -> int:
        memo = [-1 for _ in range(n+1)]
        for i in range(2, n+1):
            for j in range(1, i):
                memo[i] = max(memo[i], j*(i-j), j*memo[i-j])
        return memo[n]

    def integerBreak_math(self, n: int) -> int:
        """
        fastest
        """
        if n <=3:
            return n -1
        # encode as many 3 as component as possible
        res = 1
        while n > 4:
            n -= 3
            res *= 3
        return res * n

    def integerBreak_math_2(self, n:int)->int:
        """
        fastest
        """
        if n <=3:
            return n -1
        if n == 4:
            return n
        # encode as many 3 as component as possible
        factor = n // 3
        if n%3 == 0:
            return 3**factor
        elif n%3 == 1:
            return 3**(factor-1)*4
        return 3**factor*2


"""
Another similar problem is to count number of possible combination of this issue
"""
def integer_devision(n: int)->int:
    memo = {1:1}
    def recursive(n):
        count = 0
        for i in range(1, n+1):
            j = n - i
            if memo.get(j):
                count += memo[j]
            else:
                memo[j] = recursive(j)
                count += memo[j]
        return count
    recursive(n)
    print(memo)
    

integer_devision(3)
# class TestSolution(TestCase):
#     def test_integerBreak(self):
#         sol = Solution()
#         assert sol.integerBreak_memo(2) == 1
#         assert sol.integerBreak_memo(10) == 36
#         assert sol.integerBreak_memo(12) == 81
# main()


# sol = Solution()
# sol.integerBreak_math(11)