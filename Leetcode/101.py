# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def is_mirror(self, left_tree, right_tree):
        if not left_tree and not right_tree:
            return True
        if not left_tree or not right_tree:
            return False
        
        return left_tree.val == right_tree.val and \
        self.is_mirror(left_tree.left, right_tree.right) and \
        self.is_mirror(left_tree.right, right_tree.left) 

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root or (not root.left and not root.right):
            return True

        if not root.left or not root.right:
            return False
        return self.is_mirror(root.left, root.right)


if __name__ == "__main__":
    from tree_utils import genTree
    s = Solution()
    assert s.isSymmetric(genTree([1,2,2,3,4,4,3]))==True
    assert s.isSymmetric(genTree([1,2]))==False
