'''
Twitter 

You run an e-commerce website and want to record the last N order ids in a log. 
Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
'''


class OrdersLog:
    def __init__(self, last_N):
        self.N = last_N
        self.log = [] 

    def record(self, order_id):
        if self.N > len(self.log):
            self.log += order_id
            return 
        del self.log[0]
        self.log += order_id
        return 
    def get_last(self, i):
        return self.log[-i]