"""
437. Path Sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

TODO
"""

from tree_utils import Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class SolutionBruteForce(object):
    def dfs(self, node, sum):
        if node == None:
            return 0
        return (1 if node.val==sum else 0) + self.dfs(node.left, sum-node.val) + self.dfs(node.right, sum-node.val)

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root==None:
            return 0
        return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

class Solution(object):
    # using hashmap
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: int
        """
        self.count = 0
        preDict = {0: 1}
        def dfs(p, target, pathSum, preDict):
            if p:
                pathSum += p.val
                self.count += preDict.get(pathSum - target, 0)
                preDict[pathSum] = preDict.get(pathSum, 0) + 1
                dfs(p.left, target, pathSum, preDict)
                dfs(p.right, target, pathSum, preDict)
                preDict[pathSum] -= 1
        dfs(root, target, 0, preDict)
        return self.count
    
    
if __name__ == "__main__":
    solution = Solution()
    tree1 = [10,5,-3,3,2,None,11,3,-2,None,1]
    t1 = Tree(tree1).root
    sum = 8
    print(solution.pathSum(t1, sum))