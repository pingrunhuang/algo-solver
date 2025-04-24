'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.


TODO: do it again
'''


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<1:
            return 0
            
        if len(s)==1 and str(s)<=26 and str(s)>=1:
            return 1
        result=0
        i=len(s)-1
        lookupTable=[0 for x in range(len(s)+1)]
        
        # initialize the lookupTable
        lookupTable[len(s)]=1
        if s[i]!='0':
            lookupTable[i]=1
        i=i-1
        while i>=0:
            if s[i]!='0' and int(s[i:i+2])<=26:
                lookupTable[i]=lookupTable[i+1]+lookupTable[i+2]
            elif s[i]!='0' and int(s[i:i+2])>26:
                lookupTable[i]=lookupTable[i+1]
            i-=1
        return lookupTable[0]

if __name__=="__main__":
    solution = Solution()
    testCase1='12'
    result1=solution.numDecodings(testCase1)
    print(str(result1))
    testCase2='27'
    result2=solution.numDecodings(testCase2)
    print(str(result2))
