'''
167. Two Sum II - Input array is sorted

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int] ascending
        :type target: int
        :rtype: List[int]
        """
        if len(numbers)==0:
            return []
        head = 0
        tail = len(numbers)-1
        while head < tail:
            if numbers[head]+numbers[tail]<target:
                head+=1
            if numbers[head]+numbers[tail]>target:
                tail-=1
            if numbers[head]+numbers[tail]==target:
                return [head+1, tail+1]
        return []

if __name__ == "__main__":
    solution = Solution()
    n1 = [2, 7, 11, 15]
    t1 = 9
    print(solution.twoSum(n1, t1))
