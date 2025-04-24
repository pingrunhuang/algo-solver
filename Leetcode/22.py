'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
TODO: DP Solution
'''
class Solution:
    def recursion(self, result, temp_str, left_num, right_num):
        print(temp_str, left_num, right_num)
        if left_num==0 and right_num==0:
            result.append(temp_str)
            return
        if left_num>0:self.recursion(result, temp_str+"(", left_num-1, right_num+1)
        if right_num>0:self.recursion(result, temp_str+")", left_num, right_num-1)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.recursion(result, '', n, 0)
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))