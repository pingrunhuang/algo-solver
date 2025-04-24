'''
19. Remove Nth Node From End of List

'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next:ListNode|None = None 


class Solution:
      def removeNthFromEnd(self, head, n):
            """
            :type head: ListNode
            :type n: int
            :rtype: ListNode
            """
            dummy = ListNode(0)
            dummy.next = head
            head1 = dummy
            head2 = dummy
            distance = 0
            while head1.next:
                  if distance==n and head2.next:
                      head2=head2.next
                  else:
                      distance+=1
                  head1 = head1.next
            head2.next = head2.next.next if head2.next else None
            return dummy.next

      def removeNthFromEnd1(self, head, n):
            
            total_nodes = 0
            while head:
                  total_nodes+=1
            cur_node = head
            cur_pos = 1
            while cur_pos!=total_nodes-n:
                  cur_node=cur_node.next
                  cur_pos+=1
            cur_node.next = cur_node.next.next
            return head
        

if __name__ == "__main__":
  solution = Solution()
  t1 = [1,2,3,4,5]
  head = ListNode(t1[-1])
