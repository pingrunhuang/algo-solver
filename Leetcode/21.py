'''
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.
Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next:ListNode|None = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if not l1 and l2:
            return None
        result = ListNode(None)
        temp = result
        while l1 and l2:
            if l1.val>l2.val:
                temp.next = ListNode(l2.val)
                temp = temp.next
                l2 = l2.next
            else:
                temp.next = ListNode(l1.val)
                temp = temp.next
                l1 = l1.next
        while l1:
            temp.next = ListNode(l1.val)
            temp = temp.next
            l1 = l1.next
        while l2:
            temp.next = ListNode(l2.val)
            temp = temp.next
            l2 = l2.next
        return result.next


if __name__=="__main__":
    l13 = ListNode(4)
    l12 = ListNode(2)
    l12.next = l13
    l1 = ListNode(1)
    l1.next = l12
    l23 = ListNode(4)
    l22 = ListNode(3)
    l22.next=l23
    l2 = ListNode(1)
    l2.next=l22
    s = Solution()
    result = s.mergeTwoLists(l1, l2)
    while result:
        print(result.val)
        result = result.next