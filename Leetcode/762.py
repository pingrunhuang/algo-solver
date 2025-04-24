'''
762. Prime Number of Set Bits in Binary Representation


Notation!!!!!
We only need primes up to 19 because R <= 10^6 < 2^20
'''

class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        return sum(self.isPrime(bin(i).count('1')) for i in range(L,R+1))
    
    def isPrime(self, n):
        if n == 2 or n == 3 or n==5 or n==7 or n==11 or n==13 or n==17 or n==19:
            return True
        return False

if __name__ == '__main__':
    solution = Solution()
    L1,R1=6,10
    print(solution.countPrimeSetBits(L1, R1))
    L2,R2=10, 15
    print(solution.countPrimeSetBits(L2,R2))