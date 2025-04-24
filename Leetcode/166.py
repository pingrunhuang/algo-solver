"""
Given two integers representing the numerator and denominator of a fraction, 
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

TODO: 
"""

class Solution(object):
    def addParentheses(self, repeated_num):
        return '('+repeated_num+')'

    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator%denominator==0:
            return str(int(numerator/denominator))

        
        divided_result = str(numerator / denominator)
        integural_part, fractional_part = divided_result.split(".")
        result = integural_part + "."
        # num -> continuous apperence time
        fractional_stack = []
        for x in fractional_part:
            if len(fractional_stack) > 0:
                # hit the repeated number 
                if fractional_stack[-1] == x:
                    fractional_stack.append(x)
                # first time meeting the not repeated number
                elif fractional_stack[-1] != x and len(fractional_stack)!=1:
                    result += self.addParentheses(fractional_stack[-1])
                    fractional_stack.clear()
                    fractional_stack.append(x)
                elif fractional_stack[-1] != x and len(fractional_stack)==1:
                    result += fractional_stack.pop()
                    fractional_stack.append(x)
            elif len(fractional_stack) == 0:
                fractional_stack.append(x)
        
        # clear the rest 
        if len(fractional_stack) > 1:
            result += self.addParentheses(fractional_stack[-1])
            fractional_stack.clear()
        elif len(fractional_stack) == 1:
            result += fractional_stack.pop()

        assert len(fractional_stack) == 0
        return result

if __name__ == "__main__":
    s = Solution()
    numerator = 2
    denominator = 1
    assert s.fractionToDecimal(numerator, denominator) == "2"
    numerator = 2
    denominator = 3
    assert s.fractionToDecimal(numerator, denominator) == "0.(6)"
    numerator = 1 
    denominator = 2
    assert s.fractionToDecimal(numerator, denominator) == "0.5"
    numerator = 4
    denominator = 9
    assert s.fractionToDecimal(numerator, denominator) == "0.(4)"
    numerator = 4
    denominator = 333
    assert s.fractionToDecimal(numerator, denominator) == "0.(012)"
