'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,
    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.

DFS: note that dfs generally require a helper method for recording the cummulated result
'''

from tree_utils import genTree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs (self, root, cumulated_sum):
        if not root:
            return 0
        if root.left == None and root.right == None:
            return root.val + cumulated_sum*10
        return self.dfs(root.left, cumulated_sum*10 + root.val) + self.dfs(root.right, cumulated_sum*10 + root.val)

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, 0)

if __name__ == "__main__":
    solution = Solution()
