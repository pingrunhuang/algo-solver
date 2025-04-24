"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        is_negative = (dividend>0 and divisor<0) or (dividend<0 and divisor>0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor: # deal with divident==divisor
            cur_divisor, num_divisor = divisor, 1
            while dividend >= cur_divisor:
                dividend -= cur_divisor # dividend got substracted
                result += num_divisor
                cur_divisor = cur_divisor << 1 # 2*cur_divisor
                num_divisor = num_divisor << 1
        if is_negative:
            result = - result
        return max(min(result, 2**31-1), -2**31)


if __name__=="__main__":
    solution = Solution()
    print(solution.divide(7, -3))