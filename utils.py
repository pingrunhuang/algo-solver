from collections import deque
from typing import Union

'''
In order to print line by line, the answer is to maintain 2 pointers pointing to the current line's end and the next line's end
'''


def assertion_print(output, expected):
    print(f"output: {output}, expected: {expected}")


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left:Union[TreeNode, None] = None
        self.right:Union[TreeNode, None] = None

class Tree:

    def __init__(self, root:Union[TreeNode, None]):
        self.root = root

    def print(self):
        if self.root==None:
            return
        
        queue = deque()
        queue.append(self.root)
        cur_end_node = self.root
        next_end_node = self.root
        while len(queue)!=0:
            cur_node = queue.popleft()
            if cur_node.left:
                next_end_node=cur_node.left
                queue.append(cur_node.left)
            if cur_node.right:
                next_end_node=cur_node.right
                queue.append(cur_node.right)

            if cur_end_node==cur_node:
                cur_end_node = next_end_node
                print(cur_node.val)
            else:
                print(cur_node.val, end=' ')



if __name__ == "__main__":
    root=TreeNode(2)
    root.right=TreeNode(3)
    root.right.right=TreeNode(7)
    root.left=TreeNode(1)
    root.left.right=TreeNode(4)
    tree = Tree(root)
    tree.print()