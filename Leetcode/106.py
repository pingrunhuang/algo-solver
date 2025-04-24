'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

# TODO
'''

from leetcode.tree_utils import Tree, TreeNode

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder)==0:
            return None
        root = TreeNode(postorder.pop())
        root_index_in_inorder=inorder.index(root.val)

        left_inorder=inorder[:root_index_in_inorder]
        right_inorder=inorder[root_index_in_inorder+1:]
        
        # start from right since the postorder is changing constantly from right tree to left tree
        root.right=self.buildTree(right_inorder, postorder)
        root.left=self.buildTree(left_inorder,postorder)
        return root

if __name__=='__main__':
    solution = Solution()
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    result1 = Tree(solution.buildTree(inorder, postorder))
    result1.viewTreeBFS()

