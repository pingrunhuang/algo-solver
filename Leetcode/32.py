"""
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring


"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        if not s:
            return res
        


        return res
    



if __name__ == "__main__":
    sol = Solution()
    s = "(()"
    assert sol.longestValidParentheses(s) == 2
    s = ")()())"
    assert sol.longestValidParentheses(s) == 4
    