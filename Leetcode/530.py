from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, node: TreeNode, next: Optional[TreeNode], min_diff)->int:
        if next is None:
            return min_diff
        else:
            min_diff = min(min_diff, abs(node.val-next.val))
            left = self.traverse(node, next.left, min_diff)
            right = self.traverse(node, next.right, min_diff)
            return min(min_diff, left, right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return int(float('inf'))
        left = min(self.traverse(root, root.left, float('inf')), self.getMinimumDifference(root.left))
        right = min(self.traverse(root, root.right, float('inf')), self.getMinimumDifference(root.right))
        return min(left, right)