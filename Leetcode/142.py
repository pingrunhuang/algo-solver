'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?

    我们可以使用两枚指针oneStep、twoStep，每次分别移动1、2步，若存在圈，则两枚指针在第1、2、3、4...n圈后终会相遇(我们并不知道会在第几圈相遇)
    整个圈：1 -> 2 -> 3 -> 1
    部分圈：1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 5(跟5相连，形成圈)
           |<--------s------->| |<----------------------------r------------------------>|
           |<--------------------k----------------------->|
           |<------------------------------------2k--------------------------------------  
                                 ------------------------>|
           我们假设链表头到圈始点长度为s，圈长度为r，移动两枚指针后，相遇时oneStep走了k步，twoStep则走了2k步：
           1. 我们知道相遇时twoStep比oneStep多走了n圈，(1)(2k - s) - (k - s) = nr  =>  k = nr  =>  k = r (n = 1)
              (注意：我们取n = 1，即twoStep比oneStep多走一圈，因为一旦相遇我们便知道了有圈)

            k = r 于是便有了下面这幅图：
    部分圈：1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 5(跟5相连，形成圈)
           |<--------s------->| |<----------------------------r------------------------>|        
           |<--------------------r----------------------->|
           |<------------------------------------2r--------------------------------------  
                                 ------------------------>|
           2. s(我们知道s就是我们要求的圈始点)怎么求呢？
       
           3. 眼尖的同学可能已经看出来了，没错 s + r = 链表总长度，我们再将oneStep或者twoStep移动s就会再次相遇！
           
           于是便有了下面这幅图：
    部分圈：1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 5(跟5相连，形成圈)
           |<--------s------->| |<----------------------------r------------------------>|        
           |<--------------------r----------------------->| |************* s ************|
           |<------------------------------------2r--------------------------------------  
                                 ------------------------>| |************* s ************|
          
          4. 现在我们让oneStep再次从head开始，oneStep和twoStep每次均移动一步，再次相遇就会在起始点咯！
'''


# Definition for singly-linked list.
def generateListNode(nodes, pos):
    if len(nodes)==0:
        return None
    if len(nodes)==1:
        return ListNode(nodes[0])
    
    tail = ListNode(nodes.pop())
    copy_tail = tail
    i = len(nodes)-1
    while nodes:
        cur = ListNode(nodes.pop())
        cur.next = tail
        tail = cur
        if i == pos:
            copy_tail.next = cur
        i-=1

    return cur

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return str(self.val) + "->" + str(self.next) if self.next else str(self.val) 
    # def __str__(self):
    #     return str(self.val)

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow_ptr = head
        fast_ptr = head
        hasCycle = False

        while fast_ptr and slow_ptr:
            if fast_ptr.next:
                fast_ptr = fast_ptr.next.next
            else:
                # no cycle 
                break
            slow_ptr = slow_ptr.next
            if slow_ptr==fast_ptr:
                hasCycle = True
                break
        if hasCycle:
            fast_ptr = head
        else:
            return None
        while fast_ptr != slow_ptr:
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
        return fast_ptr

if __name__ == "__main__":
    solution = Solution()
    nodes = [3,2,0,-4]
    pos = 1
    result = solution.detectCycle(generateListNode(nodes, pos))
    assert result.val == 2

    nodes = [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]
    pos = 24
    result = solution.detectCycle(generateListNode(nodes, pos))
    print(result.val)
    
    assert result.val == 21