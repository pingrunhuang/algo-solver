class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_pair = a.split(sep='+')
        a_constant = a_pair[0]
        a_alpha = a_pair[1][:len(a_pair[1])-1]
        b_pair = b.split(sep='+')
        b_constant=b_pair[0]
        b_alpha = b_pair[1][:len(b_pair[1])-1]
        result = str(int(a_constant)*int(b_constant) - int(a_alpha)*int(b_alpha))
        result += '+' + str(int(a_constant)*int(b_alpha)+int(b_constant)*int(a_alpha)) + 'i'
        return result


if __name__=='__main__':
    solution = Solution()
    print(solution.complexNumberMultiply('1+-1i', '1+-1i'))