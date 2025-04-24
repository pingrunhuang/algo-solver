from tree_utils import Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        cur_ptr = root
        next_right = root
        cur_right = root
        result = []
        que = [root]
        while que:
            cur_ptr = que.pop(0)
            if cur_ptr.left:
                que.append(cur_ptr.left)
                next_right = cur_ptr.left
            if cur_ptr.right:
                que.append(cur_ptr.right)
                next_right = cur_ptr.right
            if cur_ptr == cur_right:
                result.append(cur_ptr.val)
                cur_right = next_right
        return result


if __name__ == "__main__":
    s = Solution()
    t = [1,2,3,None,5,None,4]
    root = Tree.genTree(t)
    s.rightSideView(root)
        