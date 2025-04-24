'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
'''
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=="0" or num2=="0":
            return "0"
        result = 0
        reversed_num1 = reversed(num1)
        reversed_num2 = reversed(num2)
        for i,vi in enumerate(reversed_num1):
            a = (10**i)*int(vi)
            for j,vj in enumerate(reversed_num2):
                b = (10**j)*int(vj)
                result+=a*b
            reversed_num2 = reversed(num2)
        result = str(result)
        return result

        

if __name__ == "__main__":
    s = Solution()
    t = ("2","3")
    assert s.multiply(t[0], t[1]) == "6"
    t = ("123", "456")
    assert s.multiply(t[0], t[1]) == "56088"
