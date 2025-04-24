'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
'''

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle=='' or haystack==needle:
            return 0
        
        needle_length = len(needle)
        for i in range(len(haystack)-needle_length+1):
            if needle == haystack[i:i+needle_length]:
                return i
        return -1

if __name__ == "__main__":
    s = Solution()
    haystack = "hello"
    needle = "ll"
    print(s.strStr(haystack, needle))



        
        
