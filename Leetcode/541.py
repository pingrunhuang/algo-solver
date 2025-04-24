'''
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

Example:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Restrictions:
    The string consists of lower English letters only.
    Length of the given string and k will in the range [1, 10000]

'''

class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s)<=k:
            reversed_str=reversed(s)
            result = ''
            for x in reversed_str:
                result+=x
            return result
        if len(s)>k and len(s)<=2*k:
            reversed_str=reversed(s[:k])
            result = ''
            for x in reversed_str:
                result+=x
            result = result+s[k:]
            return result
        result = ''
        for i in range(len(s)//(2*k)):
            result+=self.reverseStr(s[i*2*k:(i+1)*2*k], k)
        index_rest = (len(s)//(2*k))*2*k
        result = result+self.reverseStr(s[index_rest:],k) 
        return result

if __name__=='__main__':
    solution = Solution()
    testCase1='abcdefg'
    print(solution.reverseStr(testCase1, 2))