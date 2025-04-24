
'''
Nim game
You can always win a Nim game if the number of stones nn in the pile is not divisible by 4.

'''

class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n%4!=0

if __name__=='__main__':
    solution = Solution()
    print(solution.canWinNim(5))