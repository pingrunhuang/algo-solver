'''
Given a list, rotate the list to the right by k places, where k is non-negative.

Example: 
Given 1->2->3->4->5->NULL and k = 2,

return 4->5->1->2->3->NULL.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None or k==0:
            return head
        queue = []
        tail = head
        while tail:
            queue.append(tail)
            tail = tail.next
        # # we can skip the recursion here
        k =  k % len(queue)
        for _ in range(k):
            tail = queue.pop()
            queue[-1].next=None
            tail.next = queue[0]
            queue.insert(0, tail)
            print_list(queue[0])
        return queue[0]
        

def print_list(head):
    while head:
        print(head.val,end="->")
        head=head.next
    print()

if __name__ == "__main__":
    solution = Solution()
    t1 = ListNode(1)
    t1.next = ListNode(2)
    t1.next.next = ListNode(3)
    t1.next.next.next = ListNode(4)
    t1.next.next.next.next = ListNode(5)
    result1 = solution.rotateRight(t1, 2)
    print_list(result1)

    t2 = ListNode(0)
    t2.next = ListNode(1)
    t2.next.next = ListNode(2)
    result2 = solution.rotateRight(t2, 4)
    print_list(result2)

    t3 = ListNode(9)
    t3.next = ListNode(10)
    result3 = solution.rotateRight(t3, 2)
    print_list(result3)

    t4 = ListNode(1)
    t4.next = ListNode(2)
    t4.next.next = ListNode(3)
    result4 = solution.rotateRight(t4, 2000000000)
    print_list(result4)