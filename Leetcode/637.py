'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
'''
from tree_utils import Tree

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result = []
        cur_last_node = root
        next_last_node = root
        level_sum=0
        level_nodes_num=0
        queue=[]
        queue.insert(0, root)
        while len(queue)!=0:
            cur_node = queue.pop()
            if cur_node.left:
                next_last_node = cur_node.left
                queue.insert(0,cur_node.left)
            if cur_node.right:
                next_last_node = cur_node.right
                queue.insert(0,cur_node.right)
            level_sum+=cur_node.val
            level_nodes_num+=1
            if cur_node is cur_last_node:
                cur_last_node=next_last_node
                result.append(level_sum/level_nodes_num)
                level_nodes_num=0
                level_sum=0
        return result
            
            


if __name__=='__main__':
    solution = Solution()
    tree= Tree([3,9,20,15,17])
    tree.viewTreeBFS()
    print(solution.averageOfLevels(tree.root))
    