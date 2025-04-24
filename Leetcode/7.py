'''
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2**31,  2**31 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
class Solution:
    def is_more_32_bits(self, x):
        return x<-2**31 or x>2**31-1

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if self.is_more_32_bits(x):
            return 0
        stack = list()
        if x>=0:
            while x>0:
                stack.insert(0, x%10)
                x=int(x/10)
            result=0
            while len(stack)!=0:
                # this could cause the result to have more then 32 bits
                result=result*10+stack.pop()
                if self.is_more_32_bits(result):
                    return 0
            return result
        else:
            return -self.reverse(-x)

if __name__ == "__main__":
    s = Solution()
    t1 = -123
    print(s.reverse(t1))
    t2 = 1534236469
    print(s.reverse(t2))
    t3 = 900000
    print(s.reverse(t3))