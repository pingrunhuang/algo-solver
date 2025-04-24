#/usr/bin/python
#coding=utf-8

'''
Description:
Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.
'''
from functools import reduce

class Solution:
    def sumAscii(self, s):
        sum=0
        for x in s:
            sum+=ord(x)
        return sum

    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp = [[0 for _ in s1] for _ in s2]
        for row in dp:
            row[len(s1)-1] = self.sumAscii(s1[:i])
        dp[len(s2)-1] = [self.sumAscii()]
        



if __name__=='__main__':
    solution = Solution()
    t1_str1 = 'sea'
    t1_str2 = 'eat'
    print(solution.minimumDeleteSum(t1_str1, t1_str2))
    t2_str1 = 'delete'
    t2_str2 = 'leet'
    print(solution.minimumDeleteSum(t2_str1, t2_str2))