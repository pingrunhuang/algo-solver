"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def get_height(node, height):
            if not node:
                return height
            left = get_height(node.left, height + 1)
            right = get_height(node.right, height + 1)
            return max(left, right)

        left_h = get_height(root.left, 0)
        right_h = get_height(root.right, 0)

        if abs(left_h - right_h) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


if __name__ == "__main__":
    from leetcode.tree_utils import Tree

    s = Solution()
    t1 = Tree([3, 9, 20, None, None, 15, 7])
    print(s.isBalanced(t1.root))
    t2 = Tree([1, 2, 2, 3, 3, None, None, 4, 4])
    print(s.isBalanced(t2.root))
    t3 = Tree([1, 2, 2, 3, None, None, 3, 4, None, None, 4])
    print(s.isBalanced(t3.root))
