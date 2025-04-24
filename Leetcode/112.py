'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''
from leetcode.tree_utils import Tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs(self, cur, cur_sum, sum):
        if not cur:
            return False
        
        cur_sum += cur.val
        if not cur.left and not cur.right and cur_sum==sum:
            return True
        
        return self.dfs(cur.left, cur_sum, sum) or self.dfs(cur.right, cur_sum, sum)
    
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.dfs(root, 0, sum)
        

if __name__ == "__main__":
    solution = Solution()
    tree1 = [5,4,8,11,None, 13, 4, 7,2,None, None, None,1]
    t1 = Tree(tree1)
    target1 = 22
    print(solution.hasPathSum(t1.root, target1))
    tree2 = [1,2]
    t2 = Tree(tree2)
    target2 = 1
    print(solution.hasPathSum(t2.root, target2))

