'''
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

BST
'''


from tree_utils import Tree
class Solution(object):
    
    def reload_the_set(self, root, unique_ele):
        unique_ele.add(root.val)
        if root.left:
            self.reload_the_set(root.left, unique_ele)
        if root.right:
            self.reload_the_set(root.right, unique_ele)
        if not root.left and not root.right:
            return

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        unique_eles = set()
        self.reload_the_set(root, unique_eles)
        sorted_set = sorted(unique_eles)
        if len(sorted_set)<=1:
            return -1
        else:
            return sorted_set[1]
        
if __name__ == "__main__":
    solution = Solution()
    tree1 = Tree([2, 2, 5, None, None, 5, 7])
    print(solution.findSecondMinimumValue(tree1.root))
    tree2 = Tree([2,2,2])
    print(solution.findSecondMinimumValue(tree2.root))