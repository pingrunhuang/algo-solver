class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapper = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        prev_value = 0
        for i in s:
            if mapper[i]>prev_value:
                result += mapper[i] - 2*prev_value
            else:
                result += mapper[i]
            prev_value = mapper[i]
        return result

if __name__ == "__main__":
    s = Solution()
    t1 = 'III'
    print(s.romanToInt(t1))
    t2 = 'IV'
    print(s.romanToInt(t2))
    t3 = 'LVIII'
    print(s.romanToInt(t3))
    t4 = 'MCMXCIV'
    print(s.romanToInt(t4))