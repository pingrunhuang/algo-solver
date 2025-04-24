"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.container = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.container.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        self.container.pop(-1)
        

    def top(self):
        """
        :rtype: int
        """
        return self.container[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        result = self.container[0]
        for x in self.container:
            if x<result:
                result = x
        return result
        

if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
    print(param_3)
    print(param_4)