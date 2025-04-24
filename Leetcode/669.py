#!/bin/python

import unittest
from tree_utils import Tree

'''
Given a binary search tree and the lowest and highest boundaries as L and R, 
trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, 
so the result should return the new root of the trimmed binary search tree.

HINT:
BST:
LEFT < ROOT < RIGHT

TODO
'''

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root==None:
            return None
        # I was writing this block before and get an error the null node with 0 value
        # if root.left==None and root.right==None:
        #     return root

        if root.val<=R and root.val>=L:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root
        # else:
        #     if root.val > R:
        #         return self.trimBST(root.left)
        #     if root.val < L:
        #         return self.trimBST(root.right)
