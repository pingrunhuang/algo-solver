'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

Floyd's cycle-finding algorithm
https://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow_ptr = head
        fast_ptr = head
        iteration = 1
        while True:
            if fast_ptr:
                fast_ptr = fast_ptr.next
            else:
                return False
            if iteration%2==0 and slow_ptr:
                slow_ptr = slow_ptr.next
            if slow_ptr==fast_ptr:
                return True
            iteration+=1
                
if __name__ == "__main__":
    solution = Solution()
    