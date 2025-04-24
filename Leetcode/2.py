from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = l1, l2
        head = ListNode()
        ptr = head
        forward = 0
        
        while ptr1 or ptr2:
            new_node = ListNode()
            ptr.next = new_node
            if ptr1 and ptr2:
                val = ptr1.val + ptr2.val + forward
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            elif ptr1:
                val = ptr1.val + forward
                ptr1 = ptr1.next
            elif ptr2:
                val = ptr2.val + forward
                ptr2 = ptr2.next
            else:
                break
            figure, forward = val%10, val//10
            new_node.val = figure
            ptr = new_node
        
        if forward>0:
            ptr.next = ListNode(forward)
            
        return head.next