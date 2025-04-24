"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def toList(nodes):
    i = 0 
    head = ListNode(None)
    ptr = head
    while i < len(nodes):
        ptr.next = ListNode(nodes[i])
        ptr = ptr.next
        i+=1
    return head.next

def print_list(head: ListNode):
    str_builder = ""
    ptr = head
    while ptr:
        str_builder += "->{}".format(ptr.val)
        ptr = ptr.next
    print(str_builder)

class Solution:
    """
    Using constant space complexity means I could not rely on creating a new array of number.

    Here I use merge sort. Overall, if the stack calling is not counted into the space complexity, this method 
    """
    def sortList(self, head: ListNode):
        if not head:
            return head
        if not head.next:
            return head
        # when there are only 2 elements, sort them in place and return. Cost constant space complexity
        if not head.next.next:
            if head.val > head.next.val:
                temp = head.next
                head.next = None
                temp.next = head
                return temp
            return head
        
        # merge 2 sorted list: only stack calling will consume space
        def merge(ptr1: ListNode, ptr2:ListNode):
            if ptr1 is None and ptr2 is None:
                return None
            if ptr1 is None and ptr2:
                return ptr2
            if ptr1 and ptr2 is None:
                return ptr1
            
            if ptr1.val <= ptr2.val:
                ptr1.next = merge(ptr1.next, ptr2)
                return ptr1
            else:
                ptr2.next = merge(ptr1, ptr2.next)
                return ptr2
        
        front_ptr = head
        tail_ptr = head
        while front_ptr.next:
            if front_ptr.next.next:
                front_ptr = front_ptr.next.next
                prev = tail_ptr
                tail_ptr = tail_ptr.next
            else:
                prev = tail_ptr
                tail_ptr = tail_ptr.next
                front_ptr = front_ptr.next
        
        prev.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(tail_ptr)
        
        return merge(l1, l2)

def test1():
    head = toList([4,2,1,3])
    print_list(head)
    s = Solution()
    result = s.sortList(head)
    print_list(result)
    
def test2():
    head = toList([-1,5,3,4,0])
    print_list(head)
    s = Solution()
    result = s.sortList(head)
    print_list(result)

if __name__ == '__main__':
    test1()
    test2()