"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

TODO: Note these are typical linked list manipulations
"""

def generateList(l):
    if len(l)==0:
        return None
    
    ptr = ListNode(l[0])
    head = ptr
    i = 1
    while i<len(l):
        ptr.next = ListNode(l[i])
        ptr = ptr.next
        i+=1
    return head

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        result = [str(self.val)]
        ptr = self.next
        while ptr:
            result.append(str(ptr.val))
            ptr = ptr.next
        return "->".join(result)
        
class Solution(object):
    def reverse(self, node):
        if node is None:
            return None
        pre = None
        cur = node
        nex = node.next
        while nex:
            cur.next = pre
            pre = cur
            cur = nex
            nex = cur.next
        cur.next = pre
        return cur

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        # Exellent way of finding the middle of a linked list: find the middle of the list
        preMiddle = head
        temp = head
        while temp.next and temp.next.next:
            preMiddle = preMiddle.next
            temp = temp.next.next

        # reverse the half after middle
        preMiddle.next = self.reverse(preMiddle.next)
        # start reorder: cut from the preMiddle
        p1 = head
        p2 = preMiddle.next
        preMiddle.next = None
        while p1.next:
            p1_next = p1.next
            p2_next = p2.next
            p1.next = p2
            p2.next = p1_next
            p1 = p1_next
            p2 = p2_next
        if p2:
            p1.next = p2

        print(head)
        return head
        
if __name__ == "__main__":
    s = Solution()
    t = generateList([1,2,3,4])
    s.reorderList(t)
    t = generateList([1,2,3,4,5])
    s.reorderList(t)
    t = generateList([1,2])
    # print(s.reverse(t))
