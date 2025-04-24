# /usr/bin/python
# coding=utf-8

'''
Given a string, your task is to count how many palindromic substrings in this string.
The basic idea of palindrom problem is to loop the center of the string
'''

class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        if N == 0:
            return 0
        if N == 1:
            return 1
        count=0
        # expand from the center to both side 
        # center is either between 2 char or is on a char
        for center in range(2*N-1):
            left=int(center/2)
            right=left+center%2
            while left>=0 and right<N and s[left]==s[right]:
                print("right:", right, "left:", left, "center:",int(center/2))
                count+=1
                left-=1
                right+=1
        return count
        

if __name__ == "__main__":
    solution = Solution()
    test_case1 = "abc"
    # print(solution.countSubstrings(test_case1))
    test_case2 = "aaa"
    print(solution.countSubstrings(test_case2))
    test_case3 = "fdsklf"
    # print(solution.countSubstrings(test_case3))