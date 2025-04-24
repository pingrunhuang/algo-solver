class Solution:
    def has_more_32_bits(self, x):
        return x<-2**31 or x>2**31-1
    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """
        if string=='':
            return 0
        string = string.strip().split()
        if len(string)==0:
            return 0
        string = string[0]
        if string[0] not in ['-', '+'] and not string[0].isdigit():
            return 0
        # find the first sequence of numberic
        sign = -1 if string[0]=='-' else 1
        value, i = 0, 1 if string[0] in ['-','+'] else 0
        while i < len(string) and string[i].isdigit():
            value = value * 10 + int(string[i])
            i+=1
        value = sign*value
        if self.has_more_32_bits(value):
            return 2**31-1 if value >0 else -2**31
        else:
            return value

if __name__ == '__main__':
    s = Solution()
    t1 = "words and 987"
    print(s.myAtoi(t1))
    t2 = "4193 with words"
    print(s.myAtoi(t2))
    t3 = "-91283472332"
    print(s.myAtoi(t3))
    t4 = '3.14159'
    print(s.myAtoi(t4))
    t5 = ''
    print(s.myAtoi(t5))
    t6 = '    -42'
    print(s.myAtoi(t6))
    t7 = '+1'
    print(s.myAtoi(t7))
