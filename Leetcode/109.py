"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generate_tree(self, nums, left, right):
        if left > right:
            return None
        mid = left + (right - left) // 2
        root = TreeNode(nums[mid])
        root.left = self.generate_tree(nums, left, mid - 1)
        root.right = self.generate_tree(nums, mid + 1, right)
        return root

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        array = []
        while head:
            array.append(head.val)
            head = head.next
        return self.generate_tree(array, 0, len(array) - 1)


class Solution2:
    """
    2 step at a time
    1 step at a time
    """

    def to_BST(self, head, tail):
        if head == tail:
            return None
        slow = head
        fast = head
        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next
        root = TreeNode(slow.val)
        root.left = self.to_BST(head, slow)
        root.right = self.to_BST(slow.next, tail)
        return root

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        return self.to_BST(head, None)
