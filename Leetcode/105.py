'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

    1
   / \
  2   3
 / \   \
4   5   6 
       / \
      7   8
       \
        9
preorder = [1  ,2,4,5,  3,6,7,9,8]
inorder = [4,2,5,  1  ,3,7,9,6,8]
Note:
Exellent!
TODO:
THINK ABOUT THE DIFFERENCE BETWEEN 105 AND 106
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from leetcode.tree_utils import TreeNode, Tree

class Solution:
    def buildTree(self, preorder, inorder)->TreeNode:
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # given a preorder list, we know the first element is the root
        if len(inorder)==0:
            return None
        root = TreeNode(preorder.pop(0))
        root_index_in_inorder = inorder.index(root.val)
        # split the inorder list into 2 part
        left_tree_inorder = inorder[:root_index_in_inorder]
        right_tree_inorder = inorder[root_index_in_inorder+1:]

        root.left = self.buildTree(preorder, left_tree_inorder)
        root.right = self.buildTree(preorder, right_tree_inorder)
        return root

if __name__=='__main__':
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    solution = Solution()
    root = solution.buildTree(preorder, inorder)
    tree = Tree(root)
