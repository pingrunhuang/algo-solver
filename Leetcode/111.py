"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import Optional

class Solution:

    def minDepth(self, root)->int:
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        if root and not root.left and not root.right:
            return 1

        if root.left:
            left_depth = 1 + self.minDepth(root.left)
        else:
            left_depth = 0
        if root.right:
            right_depth = 1 + self.minDepth(root.right)
        else:
            right_depth = 0
        if right_depth and left_depth:
            return min(left_depth, right_depth)
        elif right_depth:
            return right_depth
        else:
            return left_depth


if __name__ == "__main__":
    from leetcode import Tree
    s = Solution()
    t1 = Tree([1,2])
    t1.viewTreeBFS()
    print(s.minDepth(t1.root))


