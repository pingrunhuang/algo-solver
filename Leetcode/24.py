# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next:ListNode|None = None

class Solution:
    def swapPairs_rec(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p1 = head
        p2 = head.next
        temp = p2.next
        p2.next = p1
        p1.next = self.swapPairs_rec(temp)
        return p2
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        head1  = head
        head2  = head.next
        result = head2
        while head1 and head2:
            head1.next = head2.next
            head2.next = head1
            head1 = head1.next
            head2=head1.next if head1 else None
        return result

if __name__ == "__main__":
    s = Solution()
    t1 = ListNode(1)
    t1.next = ListNode(2)
    t1.next.next = ListNode(3)
    t1.next.next.next = ListNode(4)
    result = s.swapPairs(t1)
    while result:
        print(result.val)
        result = result.next