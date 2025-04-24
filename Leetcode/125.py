'''

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==0:
            return True
        p1 = 0
        p2 = len(s)-1
        while p1 < p2:
            '''
            isalnum(): Return True if all characters in S are alphanumeric
            and there is at least one character in S, False otherwise.
            similar: 
            isalnum(       isalpha(       isdecimal(     isdigit(        isidentifier(  islower(       isnumeric(     isprintable(         isspace(       istitle(       t.isupper(
            '''
            # notice the p1<p2 must be required here
            # otherwise will raise index error
            while not s[p1].isalnum() and p1<p2:
                p1+=1
            while not s[p2].isalnum() and p1<p2:
                p2-=1
            if s[p1].lower()!=s[p2].lower():
                return False
            p1+=1
            p2-=1
        return True

if __name__ == "__main__":
    solution = Solution()
    t1 = "A man, a plan, a canal: Panama"
    print(solution.isPalindrome(t1))
    t2 = "race a car"
    print(solution.isPalindrome(t2))
    t3 = " "
    print(solution.isPalindrome(t3))
    t4 = ".,"
    print(solution.isPalindrome(t4))