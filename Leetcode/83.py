'''
Given a sorted linked list, delete all duplicates such that each element appear only once.
'''

def generate_list(nodes):
    p1 = ListNode(None)
    head = p1
    i = 0
    while i < len(nodes):
        p1.next = ListNode(nodes[i])
        p1=p1.next
        i+=1
    return head.next


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = head
        while head:
            while head.next and head.val == head.next.val:
                head.next = head.next.next
            head = head.next
        return result

class Solution1:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = head
        while head:
            if head.next and head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return result


class Solution2:
    # recursion is more faster
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        
        head.next = self.deleteDuplicates(head.next)
        return head.next if head.val == head.next.val else head


if __name__ == "__main__":
    #  1->1->2->3->3
    s = Solution2()
    t = s.deleteDuplicates(generate_list([1,1,2,3,3]))
    
    while t:
        print(t.val)
        t=t.next   

