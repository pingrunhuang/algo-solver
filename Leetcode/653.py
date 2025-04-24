# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inOrder(self, root, bstArr):
        if not root:
            return 
        
        if root.left:
            self.inOrder(root.left, bstArr)
        bstArr.append(root.val)
        if root.right:
            self.inOrder(root.right, bstArr)
        return bstArr

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        ordered_tree = self.inOrder(root, [])
        p1 = 0
        p2 = len(ordered_tree)-1
        while p1 < p2:
            if ordered_tree[p1]+ordered_tree[p2]==k:
                return True
            elif ordered_tree[p1]+ordered_tree[p2]<k:
                p1+=1
            else:
                p2-=1
        return False
                
        


if __name__ == "__main__":
    solution = Solution()
    head1 = TreeNode(5)
    head1.left = TreeNode(3)
    head1.right = TreeNode(6)
    head1.left.left = TreeNode(2)
    head1.left.right = TreeNode(4)
    head1.right.right = TreeNode(7)

    print(solution.inOrder(head1, []))
    print(solution.findTarget(head1, 9))
