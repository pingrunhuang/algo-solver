'''
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].
'''

class Solution(object):
    def manipulate(self, node, result):
        if node:
            if node.left:
                self.manipulate(node.left, result)
            result.append(node.val)
            if node.right:
                self.manipulate(node.right, result)
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.manipulate(root, result)
        return result

from tree_utils import Tree
if __name__ == "__main__":
    solution = Solution()
    tree1 = [1,None, 2, None, None, 3, None]
    t1 = Tree.genTree(tree1)
    print(solution.inorderTraversal(t1))