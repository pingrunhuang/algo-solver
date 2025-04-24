"""
Inorder (Left, Root, Right) 
Preorder (Root, Left, Right) 
Postorder (Left, Right, Root)
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            cur = stack.pop()
            result.append(cur.val)
            # stack FILO
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return result