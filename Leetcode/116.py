"""
116. Populating Next Right Pointers in Each Node

recursion dfs 
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root:Node) -> Node:
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        self.dfs(root.left, root.right)
        return root
    
    def dfs(self, left:Node, right:Node):
        if left is None or right is None:
            return
        left.next = right
        self.dfs(left.left, left.right)
        self.dfs(left.right, right.left)
        self.dfs(right.left, right.right)
        
