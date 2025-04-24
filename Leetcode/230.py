'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.unique_set = set()
        def dfs(cur_node):
            if cur_node:
                self.unique_set.add(cur_node.val)
                dfs(cur_node.left)
                dfs(cur_node.right)
        dfs(root)
        return sorted(self.unique_set)[k-1]

class Solution2(object):
    def kthSmallest(self, root, k):
        pass

from tree_utils import Tree
if __name__ == "__main__":
    solution = Solution()
    tree = [1]
    t =Tree(tree).root
    print(solution.kthSmallest(t, 1))
