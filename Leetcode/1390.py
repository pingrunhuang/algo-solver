"""
Four divisors
"""
import math
from typing import List
class Solution:
    def divisors(self, n:int) -> List[int]:
        """
        this is the core algo to list all the divisors with O(sqrt(n)) instead of O(n)
        """
        i = 1
        result = []
        while i <= math.sqrt(n):
            if n % i == 0:
                result.append(i)
                if i != n//i:
                    result.append(n//i)
            i += 1
        return result

    def sumFourDivisors(self, nums: List[int]) -> int:
        answer = 0
        for n in nums:
            result = self.divisors(n)
            if len(result) == 4:
                answer += sum(result)
        return answer