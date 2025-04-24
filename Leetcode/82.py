'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def generate_list(nodes):
    p1 = ListNode(None)
    head = p1
    i = 0
    while i < len(nodes):
        p1.next = ListNode(nodes[i])
        p1=p1.next
        i+=1
    return head.next


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        virtual_head = ListNode(None)
        virtual_head.next = head
        ptr1=head
        ptr2=virtual_head
        while ptr1:
            while ptr1.next and ptr1.val == ptr1.next.val:
                ptr1=ptr1.next
            
            if ptr2.next==ptr1:
                ptr2=ptr1
            else:
                ptr2.next = ptr1.next
            ptr1 = ptr1.next
        return virtual_head.next


if __name__ == "__main__":
    s = Solution()
    t = s.deleteDuplicates(generate_list([1,2,3,3,3,4,5]))

    while t:
        print(t.val)
        t=t.next