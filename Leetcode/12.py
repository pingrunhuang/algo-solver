'''
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
'''
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        init = {
            1000:'M',
            900:'CM',
            500:'D',
            400:'CD',
            100:'C',
            90:'XC',
            50:'L',
            40:'XL',
            10:'X',
            9:'IX',
            5:'V',
            4:'IV',
            1:'I'
        }
        if init.get(num):
            return init.get(num)
        keys = (1000,900,500,400,100,90,50,40,10,9,5,4,1)
        result = []
        for k in keys:
            while num>=k:
                num -= k
                result.append(init[k])
        return ''.join(result)


if __name__ == "__main__":
    s = Solution()
    t1 = 3
    assert s.intToRoman(t1)=='III'
    t2 = 58
    assert s.intToRoman(t2)=='LVIII'
    t3 = 1994
    assert s.intToRoman(t3)=='MCMXCIV'
    t4= 20
    assert s.intToRoman(t4)=='XX'