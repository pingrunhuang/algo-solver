'''
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
    The given integer is guaranteed to fit within the range of a 32-bit signed integer.
    You could assume no leading zero bit in the integer’s binary representation.

Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:

Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
'''
from functools import reduce

class Solution:
    def decimal_to_binary(self, decimal):
        b_num = []
        while decimal>=1:
            b_num.insert(0, decimal%2)
            decimal=decimal//2
        # return  reduce(lambda x,y:str(x)+str(y), b_num)
        return b_num
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = 0
        binary = self.decimal_to_binary(num)
        for i,s in enumerate(reversed(binary)):
            if s==0:
                result+=2**i
        return result
            

        

    
if __name__=='__main__':
    solution=Solution()
    print(solution.findComplement(5))

    
    