"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Solution: queue
"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = set(['+', '-', '*', '/'])
        # result = self.dfs(tokens, 0)
        stack = []
        while tokens:
            head = tokens.pop(0)

            if head in operators:
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                if head=='+':
                    stack.append(str(n1 + n2))
                elif head=='-':
                    stack.append(str(n1 - n2))
                elif head=='*':
                    stack.append(str(n1 * n2))
                elif head=='/':
                    stack.append(str(int(n1 / n2)))     
            else:
                stack.append(head)
        result = int(stack.pop())
        return result

if __name__ == "__main__":
    s = Solution()
    t1 = ["2", "1", "+", "3", "*"]
    assert s.evalRPN(t1) == 9
    t2 = ["4", "13", "5", "/", "+"]
    assert s.evalRPN(t2) == 6
    t3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    assert s.evalRPN(t3) == 22