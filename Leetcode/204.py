class Solution(object):
    def isPrime(self, n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i**2 <= n:
            if n%i == 0:
                return False
            i += 1
        return True

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 0
        res = 0
        for i in range(n):
            if self.isPrime(i):
                print(i)
                res += 1
        return res

if __name__ == "__main__":
    s = Solution()
    t = 10
    res = s.countPrimes(t)
    print(res)
    t = 499979
    res = s.countPrimes(t)
    print(res)
    t = 999983
    res = s.countPrimes(t)
    print(res)