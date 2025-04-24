'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, 
then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]


ideas of BFS
'''
from tree_utils import Tree
import unittest
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        que = deque()
        que.append(root)
        cur_end_node = root
        next_end_node = root
        result = []
        i=1
        level_nodes=[]
        while que:
            cur_node = que.popleft()
            if cur_node!=None and cur_node.left:
                que.append(cur_node.left)
                next_end_node=cur_node.left
            if cur_node!=None and cur_node.right:
                que.append(cur_node.right)
                next_end_node=cur_node.right
            
            if cur_node==cur_end_node:
                cur_end_node=next_end_node
                if cur_node.val!=None:
                    level_nodes.append(cur_node.val)

                if i%2==1:
                    result.append(level_nodes)
                else:
                    result.append(list(reversed(level_nodes)))
                i+=1
                level_nodes=[]
            else:
                if cur_node.val!=None:
                    level_nodes.append(cur_node.val)
        return result
            
        

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.testCase1 = Tree([3,9,20,None,None,15,7])
    def testZigzagLevelOrder(self):
        self.assertEqual([[3],[20,9],[15,7]], self.solution.zigzagLevelOrder(self.testCase1.root))
        

if __name__=='__main__':
    unittest.main()