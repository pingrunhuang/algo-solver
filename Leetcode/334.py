'''
Write a function that takes a string as input and returns the string reversed.
'''

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=''
        i = len(s)-1
        while i>=0:
            result+=s[i]
            i-=1
        return result

if __name__=='__main__':
    solution = Solution()
    testCase1='hello'
    print(solution.reverseString(testCase1))