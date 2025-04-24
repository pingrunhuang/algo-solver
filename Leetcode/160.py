"""
160. Intersection of Two Linked Lists



"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1(object):
    def getIntersectionNode(self, headA, headB):
        """
        HashTable solution
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        traversedMap = {}
        ptr1 = headA
        ptr2 = headB
        while ptr1:
            traversedMap[ptr1] = True
            ptr1 = ptr1.next
        while ptr2:
            if traversedMap.get(ptr2):
                return ptr2
            ptr2 = ptr2.next
        return None


class Solution2(object):
    def getIntersectionNode(self, headA, headB):
        """
        Tricky soltuion
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        ptr1 = headA
        ptr2 = headB
        lenA = 0
        lenB = 0
        while ptr1:
            lenA += 1
            ptr1 = ptr1.next
        while ptr2:
            lenB += 1
            ptr2 = ptr2.next
        ptr1=headA
        ptr2=headB
        count=0
        while count<lenA+lenB:
            if ptr1==ptr2:
                return ptr1
            # cross the pointer
            if ptr1.next:
                ptr1 = ptr1.next
            else:
                ptr1 = headB
            if ptr2.next:
                ptr2 = ptr2.next
            else:
                ptr2 = headA
            count+=1
        return None
            