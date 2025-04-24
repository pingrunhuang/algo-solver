'''
98. Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

1. The left subtree of a node contains only nodes with keys less than the node's key.
2. The right subtree of a node contains only nodes with keys greater than the node's key.
3. Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from tree_utils import genTree
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.recursion(root, None, None)
    def recursion(self, root, max_node, min_node):
        # first basic condition
        if not root:
            return True
        # second basic condition
        if (max_node and root.val >= max_node.val) or (min_node and root.val <= min_node.val):
            return False
        return self.recursion(root.left, root, min_node) and self.recursion(root.right, max_node, root)

if __name__ == "__main__":
    solution = Solution()
    tree1 = [2,1,3]
    t1 = genTree(tree1)
    print(solution.isValidBST(t1))
    tree2 = [10,5,15,None,None,6,20]
    t2 = genTree(tree2)
    print(solution.isValidBST(t2))