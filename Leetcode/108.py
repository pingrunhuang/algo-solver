"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, nums, left_index, right_index):
        if left_index>right_index:
            return None
        mid_index = left_index+(right_index-left_index)//2
        root = TreeNode(nums[mid_index])
        root.left = self.dfs(nums, left_index, mid_index-1)
        root.right = self.dfs(nums, mid_index+1, right_index)
        return root

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==0:
            return None
        return self.dfs(nums, 0, len(nums)-1)

if __name__ == "__main__":
    s=Solution()
    s.sortedArrayToBST([-10,-3,0,5,9])