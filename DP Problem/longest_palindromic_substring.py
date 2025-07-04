'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

corner case
'''

class Solution3:
    '''
    Manacher's algo
    '''
    def longestPalindrome(self, s):
        pass

class Solution2:
    '''
    Longest common sub-string With dp
    '''
    def longest_common_sub(self, s1, s2):
        rows = len(s1)
        cols = len(s2)
        # initialize the table for storing the common suffix of substrings 
        self.suffix_table = [["" for _ in range(rows+1)] for _ in range(cols+1)]
        result = ""
        for i in range(rows+1):
            for j in range(cols+1):
                if i == 0 or j == 0 :
                    self.suffix_table[i][j]=""
                elif s1[i-1] == s2[j-1]:
                    self.suffix_table[i][j]=self.suffix_table[i-1][j-1]+s1[i-1]
                    # this is used for checking if the common sub string is palindrome 
                    # omit it if we are just checking the LCS
                    # result = self.suffix_table[i][j] if len(self.suffix_table[i][j]) > len(result) else result
                    result = self.suffix_table[i][j] if len(self.suffix_table[i][j]) > len(result) and self.suffix_table[i][j]==self.suffix_table[i][j][::-1] else result
                else:
                    self.suffix_table[i][j]=""
        return result

    def longestPalindrome(self,s):
        # reverse a list s[begin:end:step]
        return self.longest_common_sub(s, s[::-1])

class Solution:

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n==0 or n==1:
            return s
        print("checking: ", s)
        start_ptr = 0
        end_ptr = 0
        # there exists n-1+n possible position for the center index
        for i in range(n):
            # handle case "racecar"
            len1= self.expand(s, i, i)
            # handle case "aabbaa"
            len2 = self.expand(s, i, i+1)
            max_len = max(len1, len2)

            if max_len > end_ptr-start_ptr:
                start_ptr = i - int((max_len-1)/2)
                end_ptr = i + int(max_len/2)
        return s[start_ptr:end_ptr+1]

    def expand(self, s, left, right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        # left and right are the index of the first non-matching character
        # the reason why need to -1 is that we need to return the length of the palindrome
        # for example, s="racecar", when it comes to left=-1 (which is the exit condistion of the previous while loop)
        # right=7, right-left=7-(-1)=8, but the length of the palindrome is 7
        return right - left - 1

    def run(self):
        t1="babad"
        t2="dcbabcde"
        t3="bb"
        t4="abac"
        t5="caba"
        t6="aacdefcaa"
        t7="cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc" # memory error for the solution2 situation
        tests = [t1, t2, t3, t4, t5, t6, t7]
        for t in tests:
            print(self.longestPalindrome(t))

if __name__ == '__main__':
    s = Solution()
    s.run()
    