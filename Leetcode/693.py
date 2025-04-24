'''
693. Binary Number with Alternating Bits
'''

from collections import deque
class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        queue=deque()
        while n!=0:
            queue.appendleft(n%2)
            if len(queue)==2:
                if queue[0]==queue[1]:
                    return False
                else:
                    queue.pop()
            n=n//2
        return True
                
        


if __name__ == '__main__':
    solution = Solution()
    t1=10
    print(solution.hasAlternatingBits(t1))
    t2=11
    print(solution.hasAlternatingBits(t2))
    t3=3
    print(solution.hasAlternatingBits(t3))
    t4=6
    print(solution.hasAlternatingBits(t4))