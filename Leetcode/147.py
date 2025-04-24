# singly linked list.
# Algorithm of Insertion Sort:

# Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
# It repeats until no input elements remain.
# sort the linked list in ascending order 
# watch this on how insertion work: https://visualgo.net/en/sorting
# TODO: before interview

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def toList(nodes)->ListNode:
    i = 0 
    head = ListNode(None)
    ptr = head
    while i < len(nodes):
        ptr.next = ListNode(nodes[i])
        ptr = ptr.next
        i+=1
    return head.next

def toStr(head: ListNode) -> ListNode:
    str_builder = ""
    ptr = head
    while ptr:
        str_builder += "->{}".format(ptr.val)
        ptr = ptr.next
    return str_builder

import sys
class Solution(object):
    """
    This is a solution 
    """
    def insert(self, node1: ListNode, node2: ListNode, node3: ListNode, node4: ListNode):
        """
        node4 -> node3 ->  ... -> node2 -> node1
        what this function does: insert node1 in between node4 and node3 

        this will actually affect the nodes address in the scope out of this function
        """
        cur = node1.next
        node2.next = node1.next
        node1.next = node3
        node4.next = node1
        return  (node2, cur, node1, node3)

    def insertionSortList(self, head: ListNode):
        """
        In this way, we eliminate the double loop as much as possible 
        node1 -> ... -> prev -> ... cur -> nex
        """
        if head is None or head.next is None:
            return head
        dummy = ListNode(-sys.maxsize)
        dummy.next = head
        prev = dummy
        cur = head
        while cur and cur.next:
            # print(toStr(head))
            # continue the cur pointer to where is a drop 
            if cur.next.val >= cur.val:
                cur = cur.next
            else:
                # smaller value found 
                # when do we need to reset the prev? 
                # this will dramatically drop the runover 
                # notice we are always comparing the next of prev and the next of cur
                # eg 1,2,3,7,8,9,4,5
                if prev.next.val > cur.next.val:
                    prev = dummy

                while prev and prev.next.val <= cur.next.val:
                    prev = prev.next

                # node1 -> ... -> prev -> ... cur -> nex
                # be careful: this will create cycle 
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = prev.next
                prev.next = tmp
                
        return dummy.next

class Solution1(object):
    """
    This is a solution timelimit exceed
    """
    def insertionSortList(self, head: ListNode):
        cur = head
        while cur:
            cur_next = cur.next
            # little bit optimization here to avoid TLE
            if cur_next and cur_next.val < cur.val:
                ptr = head         
                while ptr:
                    if ptr.val > cur_next.val:
                        # instead of swapping the whole pointer address, swapping value is more easier
                        ptr.val, cur_next.val = cur_next.val, ptr.val
                    ptr = ptr.next
            else:
                cur = cur.next
        return head

class Solution2(object):
    """
    This method is similar to the address swap one, but use value swap
    eg 1,2,3,6,7,8,9,4,5,6
    """
    def insertionSortList(self, head: ListNode):
        dummy = ListNode(-sys.maxsize)
        prev = dummy
        dummy.next = head
        cur = head
        while cur and cur.next:

            if cur.next.val >= cur.val:
                cur = cur.next
                continue
            
            # say we are at 9
            if prev.next.val >= cur.next.val:
                prev = dummy
            
            while prev.next.val < cur.next.val:
                prev = prev.next
            
            cur.next.val, prev.next.val = prev.next.val, cur.next.val
            # why we don't need it? think about when we exchange 4 and 6, and try to move ptr on 4, we will move twice
            # cur = cur.next
        return dummy.next


def test1():
    nodes = [-1,5,3,4,0]
    head = toList(nodes)
    s = Solution()
    print(toStr(s.insertionSortList(head)))

test1()    

def test2():
    nodes = [1,2,3,4]
    head = toList(nodes)
    print(toStr(head))
    s = Solution()
    result = s.insert(head.next.next.next, head.next.next, head.next, head)
    for x in result:
        print(x.val if x else "None", end=" ")
    print()
    print(toStr(head))

def test3():
    nodes = [4,19,14,5,-3,1,8,5,11,15]
    head = toList(nodes)
    s = Solution()
    print(toStr(s.insertionSortList(head)))

test2()
test3()