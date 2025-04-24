"""
BFS
"""


class Node(object):
    def __init__(self, id, val, left, right, next):
        self.id = id
        self.val = val
        self.left = left
        self.right = right
        self.next = next
    def __repr__(self):
        return str(self.id)
    def __str__(self):
        if self.left and self.right:
            return """
                {}
                /   \\
            {}      {}
            """.format(str(self.val), str(self.left),  str(self.right))
        if self.left and not self.right:
            return """
                {}
                /
            {} 
            """.format(str(self.val), str(self.left))
        if self.right and not self.left:
            return """
                {}
                    \\
                    {}
            """.format(str(self.val), str(self.right))
        else:
            return "{}".format(self.val)

def generateTree(json):
    if not json:
        return None

    left = generateTree(json.get('left'))
    right = generateTree(json.get('right'))

    root = Node(json['$id'], json['val'], left, right, json['next'])
    
    return root

class Solution(object):
    def connect(self, root:Node) -> Node:
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        tail1=root
        tail2=root
        ptr=root
        queue=[ptr]
        row = []
        while queue:
            # queue property: FIFO
            ptr = queue.pop(0)
            row.append(ptr)
            if ptr.left:
                tail2 = ptr.left
                queue.append(ptr.left)
            if ptr.right:
                tail2 = ptr.right
                queue.append(ptr.right)
            if ptr == tail1:
                tail1 = tail2
                for i in range(len(row)-1):
                    row[i].next = row[i+1]
                row.clear()
        return root
    
if __name__ == "__main__":
    t1 = {
        "$id":"1",
        "left":{
            "$id":"2",
            "left":{
                "$id":"3",
                "left":None,
                "next":None,
                "right":None,
                "val":4
            },
            "next":None,
            "right":{
                "$id":"4",
                "left":None,
                "next":None,
                "right":None,
                "val":5
            },
            "val":2
        },
        "next":None,
        "right":{
            "$id":"5",
            "left":None,
            "next":None,
            "right":{
                "$id":"6",
                "left":None,
                "next":None,
                "right":None,
                "val":7
            },
            "val":3
        },
        "val":1
    }
    root = generateTree(t1)
    s = Solution()
    result = s.connect(root)
    print(result)
    t2 = {
        "$id":"1",
        "left":{
            "$id":"2",
            "left":{
                "$id":"3",
                "left":{
                    "$id":"4",
                    "left":None,
                    "next":None,
                    "right":None,
                    "val":7
                },
                "next":None,
                "right":None,
                "val":4
            },
            "next":None,
            "right":{
                "$id":"5",
                "left":None,
                "next":None,
                "right":None,
                "val":5
            },
            "val":2
        },
        "next":None,
        "right":{
            "$id":"6",
            "left":None,
            "next":None,
            "right":{
                "$id":"7",
                "left":None,
                "next":None,
                "right":{
                    "$id":"8",
                    "left":None,
                    "next":None,
                    "right":None,
                    "val":8
                },
                "val":6
            },
            "val":3
        },
        "val":1
    }
    print(root)

