'''
A message containing letters from A-Z is being encoded to numbers using the following mapping way:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*', return the total number of ways to decode it.

Also, since the answer may be very large, you should return the output mod 10^9 + 7.

Example 1:
Input: "*"
Output: 9
Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".
Example 2:
Input: "1*"
Output: 9 + 9 = 18
Note:
The length of the input string will fit in range [1, 105].
The input string will only contain the character '*' and digits '0' - '9'.

TODO
'''


class Solution(object):
    def __init__(self):
        self.dictionary = {
            '**':15,
            '*1':9,
            '*2':9,
            '*3':9,
            '*4':9,
            '*5':9,
            '*6':9,
            '*7':9,
            '*8':9,
            '*9':9,
            '1*':9,
            '2*':6,
            '27':0,
            '28':0,
            '29':0            
        }
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        if n<1:
            return 0
        
        # initialization
        lookup = [0 for x in range(n+1)]
        lookup[n]=1
        if s[n-1]!='0' and s[n-1]!='*':
            lookup[n-1]=1
        elif s[n-1]!='0' and s[n-1]=='*':
            lookup[n-1]=9
        
        i=n-2
        while i>=0:
            if s[i]!='0':
                lookup[i]=self.dictionary[s[i:i+2]]+lookup[i+1]
            i-=1
        return lookup[0]%(10**9+7)
                


if __name__=="__main__":
    solution = Solution()
    testCase1='*'
    result1=solution.numDecodings(testCase1)
    print(str(result1))
    testCase2='1*'
    result2=solution.numDecodings(testCase2)
    print(str(result2))
    testCase3='**'
    result3=solution.numDecodings(testCase3)
    print(str(result3))
    testCase4='*1'
    result4=solution.numDecodings(testCase4)
    print(str(result4))
    testCase5='***'
    result5=solution.numDecodings(testCase5)
    print(str(result5))