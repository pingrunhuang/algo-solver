# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        row = []
        queue = [root]
        p1 = root
        p2 = root
        while queue:
            cur_node = queue.pop(0)
            row.append(cur_node.val)
            if cur_node.left:
                p2 = cur_node.left
                queue.append(cur_node.left)
            if cur_node.right:
                p2 = cur_node.right
                queue.append(cur_node.right)
            if cur_node==p1:
                p1 = p2
                result.append(row.copy())
                row.clear()
        result.reverse()
        return result

if __name__ == "__main__":
    from tree_utils import Tree
    s = Solution()
    t1 = Tree.genTree([3,9,20, None, None,15,7])
    result = s.levelOrderBottom(t1)
    print(result)
    