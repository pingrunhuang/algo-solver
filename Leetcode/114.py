'''
114. Flatten Binary Tree to Linked List
         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6

post order traverse:
    traversing require thinking about the last node
'''
from leetcode.tree_utils import Tree

class Solution:
    def __init__(self):
        '''
        previously visited node
        '''
        self.prev = None

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root==None:
            return None
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        # if root.right:
        #     root.right.right = self.prev
        root.left = None
        self.prev = root


    def pre_order_print(self, root):
        if root is None:
            return None
        print(root.val)
        self.pre_order_print(root.left)
        self.pre_order_print(root.right)


if __name__ == "__main__":
    solution = Solution()
    t1 = Tree([1,2,5,3,4,None,6])
    solution.flatten(t1.root)
    solution.pre_order_print(t1)