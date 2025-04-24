"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children. And also the node value could be negative
"""


class Solution:

    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type s: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []

        def dfs(node, valid_path):
            valid_path.append(node.val)

            if node and not node.left and not node.right and sum(valid_path)==s:
                result.append(valid_path.copy())
                valid_path.pop()
                return
            if node.left:
                dfs(node.left, valid_path)
            if node.right:
                dfs(node.right, valid_path)
            valid_path.pop()

        dfs(node=root, valid_path=[])
        return result


if __name__ == "__main__":
    from leetcode import Tree

    s = Solution()
    t1 = Tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    print(s.pathSum(t1.root, 22))
