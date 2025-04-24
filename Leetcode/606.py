'''
You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". 

And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree. 

Solutions: might use dfs
'''

from collections import deque

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ''
        
        if t.left and t.right:
            return str(t.val) + "(" + self.tree2str(t.left) + ")" + "(" + self.tree2str(t.right) + ")"
        if t.left and not t.right:
            return str(t.val) + "(" + self.tree2str(t.left) + ")"
        elif not t.left and t.right:
            return str(t.val) + "()" + "(" + self.tree2str(t.right) + ")"
        elif not t.left and not t.right:
            return str(t.val)


if __name__=='__main__':
    solution = Solution()
    test1=TreeNode(1)
    test1.left=TreeNode(2)
    test1.right=TreeNode(3)
    test1.left.left=TreeNode(4)
    print(solution.tree2str(test1))

    test2=TreeNode(1)
    test2.left=TreeNode(2)
    test2.right=TreeNode(3)
    test2.left.right=TreeNode(4)
    print(solution.tree2str(test2))