# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head

        pseudo_head = ListNode(None)
        pseudo_head.next = head
        cur = pseudo_head
        while cur:
            nex_ptr = cur.next
            while nex_ptr and nex_ptr.val == val:
                nex_ptr = nex_ptr.next
            cur.next = nex_ptr
            cur = nex_ptr
        return pseudo_head.next



if __name__ == "__main__":
    pass
