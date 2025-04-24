import unittest
from typing import Optional, List, Union


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class Tree:
    def __init__(self, data: Union[List, TreeNode, None]):
        if isinstance(data, List):
            self.root = self.genTree(data)
        elif isinstance(data, TreeNode):
            self.root = data
        else:
            self.root = None

    @staticmethod
    def genTree(arr):
        '''
        input: list[int]
        output: treeNode of the root
        the binary tree should always with length 2^k
        '''
        if len(arr) <= 0:
            return None

        def helper(i)->Optional[TreeNode]:
            if i < len(arr):
                if arr[i] is None:
                    return None
                else:
                    root = TreeNode(arr[i])
                    root.left = helper(2 * i + 1)
                    root.right = helper(2 * i + 2)

                    return root

        return helper(0)

    def viewTreeBFS(self, root:Optional[TreeNode]=None):
        if not root:
            if not self.root:
                return
            else:
                self.viewTreeBFS(self.root)
                return
        if not isinstance(root, TreeNode):
            print("Root of the tree should be TreeNode type")
            return
        que = [root]
        cur_end_node = root
        next_end_node = root
        while len(que) > 0:
            cur_node = que.pop(0)
            if cur_node.left is not None:
                next_end_node = cur_node.left
                que.append(cur_node.left)
            if cur_node.right is not None:
                next_end_node = cur_node.right
                que.append(cur_node.right)
            if cur_node == cur_end_node:
                cur_end_node = next_end_node
                print(cur_node.val)
            else:
                print(cur_node.val, end=' ')


class TestCases(unittest.TestCase):

    def setUp(self):
        self.testCase1 = Tree([3, 9, 20, None, None, 15, 7])
        self.testCase2 = Tree([1, None, 2, None, None, 3, None])

    def testGenTree(self):
        self.assertEqual(3, getattr(self.testCase1.root, "val"))
        self.testCase1.viewTreeBFS(self.testCase1.root)

    def testViewTree(self):
        self.testCase2.viewTreeBFS()


if __name__ == '__main__':
    unittest.main()
