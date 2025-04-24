"""
# Definition for a Node.
"""
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        node_look_up = {}
        ptr = head
        while ptr:
            node_look_up[id(ptr)] = Node(ptr.val, None, None)
            ptr = ptr.next

        ptr = head
        while ptr:
            if ptr.next:
                node_look_up[id(ptr)].next = node_look_up[id(ptr.next)]
            if ptr.random:
                node_look_up[id(ptr)].random = node_look_up[id(ptr.random)]
            ptr = ptr.next
        return node_look_up[id(head)]


if __name__ == "__main__":
    s = Solution()
    
    input = {"$id":"1","next":{"$id":"2","next":None,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
    output = {"$id":"1","next":{"$id":"2","next":None,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}