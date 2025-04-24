# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        p1 = root
        p2 = root
        row = []
        queue = [root]
        while len(queue)>0:
            cur_node = queue.pop(0)
            row.append(cur_node.val)
            if cur_node.left:
                queue.append(cur_node.left)
                p2 = cur_node.left
            if cur_node.right:
                queue.append(cur_node.right)
                p2 = cur_node.right

            if cur_node == p1:
                p1=p2
                result.append(row.copy())
                row.clear()
        return result
            

if __name__ == "__main__":
    from tree_utils import genTree
    s =Solution()
    t1 = genTree([3,9,20,None,None,15,7])
    print(s.levelOrder(t1))
    t2 = genTree([1,2,3,4,5])
    print(s.levelOrder(t2))
