'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

TODO: ASKED BY SKYSCANNER
'''

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s=='': return True
        if len(s)==1: return False
        parentheses={
            '(':')',
            '{':'}',
            '[':']'
        }
        stack = []
        for char in s:
            if char in parentheses.keys():
                stack.append(char)
            else:
                if len(stack)>0:
                    left_parentheses = stack.pop()
                    if parentheses[left_parentheses]!=char:
                        return False
                else:
                    return False
        if len(stack)!=0:
            return False
        return True

if __name__ =="__main__":
    s = Solution()
    t1 = "()"
    t2 = "()[]{}"
    t3 = "{[]}"
    t4 = "([)]"
    t5 = "){"
    print(s.isValid(t1))
    print(s.isValid(t2))
    print(s.isValid(t3))
    print(s.isValid(t4))