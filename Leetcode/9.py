'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up:

Coud you solve it without converting the integer to a string?

TODO
'''

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x%10==0 and x!=0):
            return False
        
        # to avoid the overflow situation, we use half of the interger
        reverted_half_int = 0
        while x > reverted_half_int:
            reverted_half_int = reverted_half_int*10 + x%10
            x = int(x/10)
        # deal with even and odd number of digits 
        return reverted_half_int==x or x==int(reverted_half_int/10)

    
if __name__ == "__main__":
    s = Solution()
    t1 = 121
    print(s.isPalindrome(t1))
    t2 = -121
    print(s.isPalindrome(t2))
    t3 = 10
    print(s.isPalindrome(t3))