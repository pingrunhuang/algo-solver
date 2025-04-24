import math
from typing import List

class Solution:
    def findClosest(self, num: int) -> List[int]:
        p = int(math.sqrt(num))
        while p >= 1:
            if num % p == 0:
                return [p, num//p]
            p -= 1
        return [1, num]
    
    def closesDivisors(self, num: int) -> List[int]:
        n1, n2 = num + 1, num + 2
        res1, res2 = self.findClosest(n1), self.findClosest(n2)
        return res1 if res1[1] - res1[0] < res2[1] - res2[0] else res2
