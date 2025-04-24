'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def gen_list(self, l):
        head = ListNode(l[0])
        temp = head
        for i in l[1:]:
            temp.next = ListNode(i)
            temp = temp.next
        return head
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        p1 = []
        p2 = []
        while head:
            if head.val<x:
                p1.append(head.val)
            else:
                p2.append(head.val)
            head = head.next
        print(p1 + p2)
        return self.gen_list(p1+p2)
                
if __name__ == "__main__":
    solution = Solution()
    t1 = solution.gen_list([1,4,3,2,5,2])
    target1 = 3
    result1 = solution.partition(t1, target1)
    while result1:
        print(result1.val, end="\t")
        result1 = result1.next
