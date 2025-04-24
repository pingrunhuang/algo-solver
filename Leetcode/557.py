'''
Given a string, you need to reverse the order of characters in each word within a sentence while 
still preserving whitespace and initial word order.
'''

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reversed_s=''
        for x in reversed(s):
            reversed_s+=x
        result = ''
        for word in reversed(reversed_s.split(' ')):
            result+=word+' '
        return result.strip()

if __name__=='__main__':
    solution = Solution()
    testCase1 = "Let's take LeetCode contest"
    print(solution.reverseWords(testCase1))
    