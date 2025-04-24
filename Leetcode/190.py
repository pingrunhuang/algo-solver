"""
190. Reverse Bits

Reverse bits of a given 32 bits unsigned integer.
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if n == 0:
            return 0
        bits = [0 for _ in range(32)]
        i = 31
        while n != 0:
            remain = n % 2
            n //= 2
            bits[i] = remain
            i-=1
        ret = sum([bits[i]*(2**i) for i in range(32)])
        return ret

class Solution2:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if n == 0:
            return 0
        i = 31
        ret = 0
        while n != 0:
            remain = n % 2
            ret += remain * (2**i)
            n //= 2
            i-=1
        return ret

class Solution3:
    # @param n, an integer
    # @return an integer
    # bit manipulation solution
    def reverseBits(self, n):
        ret = 0
        for _ in range(32):
            # (2**i) * n % 2
            ret = (ret<<1) + (n&1)
            n >>= 1 # n //= 2
        return ret

if __name__ == "__main__":
    s = Solution2()
    t1 = 43261596
    print(s.reverseBits(t1))