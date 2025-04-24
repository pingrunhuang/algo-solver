# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    """
    This solution is not using O(h) memory!!!!
    """
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.sorted_list = []
        self.ptr = 0
        self._inorder_traversal(root)

    def _inorder_traversal(self, root):
        """
        Important: how to recursively traverse a bst inorder
        how to do it with while loop?
        """
        if not root:
            return
        self._inorder_traversal(root.left)
        self.sorted_list.append(root.val)
        self._inorder_traversal(root.right)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        result = self.sorted_list[self.ptr]
        self.ptr += 1
        return result
        
    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if self.ptr>=len(self.sorted_list):
            return False
        return True
        
def generate_tree(nums, left, right):
    if left > right:
        return None
    mid = left + (right - left) // 2
    root = TreeNode(nums[mid])
    root.left = generate_tree(nums, left, mid - 1)
    root.right = generate_tree(nums, mid + 1, right)
    return root

if __name__ == "__main__":
    # Your BSTIterator object will be instantiated and called as such:
    t = [3,None,7,9,15,20]
    root = generate_tree(t, 0, len(t))
    obj = BSTIterator(root)
    param_1 = obj.next()
    param_2 = obj.hasNext()