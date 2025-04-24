# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1

if __name__ == "__main__":
    from leetcode.tree_utils import genTree
    s = Solution()
    t1 = genTree([3,9,20,None,None,15,7])
    print(s.maxDepth(t1))