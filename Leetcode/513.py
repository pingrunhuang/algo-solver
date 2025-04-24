from tree_utils import Tree


class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue=[root]
        cur_last_node = root
        next_last_node = root
        result = root.val
        while len(queue)!=0:
            cur_node = queue.pop(0)
            if cur_node.right:
                queue.append(cur_node.right)
                next_last_node=cur_node.right
            if cur_node.left:
                queue.append(cur_node.left)
                next_last_node=cur_node.left

            if cur_node is cur_last_node:
                cur_last_node = next_last_node
                result=cur_node.val
        return result
        



if __name__=='__main__':
    solution = Solution()
    t1 = Tree([1,2,3,4,None,5,6,7])
    print(solution.findBottomLeftValue(t1.root))
    t2 = Tree([2,1,3])
    print(solution.findBottomLeftValue(t2.root))
