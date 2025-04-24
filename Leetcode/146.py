# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# 1. easy implementation
# 2. O(1) implementation
class Node:
    def __init__(self):
        self.key = None
        self.val = None
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.length = 0

    def _del(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def append(self, node: Node):
        self._insert_head(node)
        self.length += 1
    
    def _insert_head(self, node: Node):
        node.next = self.head.next
        self.head.next.prev = node

        self.head.next = node
        node.prev = self.head

    def move_to_head(self, node: Node):
        # first delete 
        self._del(node)
        # second set the head
        self._insert_head(node)
    
    def pop_tail(self):
        """
        Pop the last one in the list for comparing
        """
        tail = self.tail.prev
        self._del(tail)
        self.length -= 1
        return tail
    
    def __str__(self):
        ptr = self.head
        string_builder = ""
        while ptr:
            string_builder += (str([ptr.key, ptr.val]) + "->")
            ptr = ptr.next
        return string_builder

class LRUCache:
    """
    Essentially use double linked list + dict to implement
    double linked list: keep track of the head(highest rank) and tail(lowest rank) 
    alternatively use collections.OrderedDict
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.query_frequency_list = DoubleLinkedList()

    def get(self, key: int):
        """
        Every time when the get method is triggered and the key exists, 2 things happened:
        1: the corresponding key query frequency gets update to the the highest rank.
        2. the corresponding value gets returned.
        """
        if self.cache.get(key) is None:
            return -1
        node = self.cache.get(key)
        self.query_frequency_list.move_to_head(node)
        value = self.cache.get(key).val
        return value

    def put(self, key: int, value: int):
        """
        When a key needs to get into the cache, 2 check happens:
        1. total cache size check
        2. rank check
        """
        # print("List length: {}".format(self.query_frequency_list.length))
        # print("Cache length: {}".format(len(self.cache)))
        assert self.query_frequency_list.length == len(self.cache)

        if self.cache.get(key) is not None:
            # key already exists, just update the value and the query frequency
            node = self.cache.get(key)
            node.val = value
            self.query_frequency_list.move_to_head(node)
            self.cache[key] = node
        else:
            node = Node()
            node.val = value
            node.key = key
            if len(self.cache) < self.capacity:
                self.query_frequency_list.append(node)
                self.cache[key] = node
            else:
                # key does not exists the key with lowest rank gets deleted
                tail = self.query_frequency_list.pop_tail()
                del self.cache[tail.key]
                self.cache[key] = node
                self.query_frequency_list.append(node)




from collections import OrderedDict
class LRUCacheWithOrderedDict(OrderedDict):
    """
    The OrderedDict in python can keep track of the insertion order
    """
    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int):
        if key not in self:
            return -1
        value = self[key]
        # move to head
        self.move_to_end(key)
        return value

    def put(self, key: int, value: int):
        """
        Put key value into the the cache will triger following checks:
        1. if the key aready exists, move that key to head 
        2. if the cache size over load, delete the last one
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)
        

    

def test1():
    cache = LRUCacheWithOrderedDict(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1)) # 1
    cache.put(3, 3)
    print(cache.get(2)) # -1
    cache.put(4, 4)
    print(cache.get(1)) #       // returns -1 (not found)
    print(cache.get(3)) #       // returns 3
    print(cache.get(4)) #       // returns 4
    # print(cache.query_frequency_list)
    # print(cache.cache)

def test2():
    cache = LRUCacheWithOrderedDict(2)
    cache.put(2,1)
    cache.put(2,2)
    print(cache.get(2)) # 2
    cache.put(1,1)
    cache.put(4,1)
    print(cache.get(2)) # -1

if __name__ == '__main__':
    test2()

            


