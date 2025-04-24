'''
Given a circular array (the next element of the last element is the first element of the array), 
print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, 
which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Note: The length of given array won't exceed 10000.
meaning the time complexity could not exceed O(N2)


Two ways of dealing with circular problems:
1. using a stack
2. add it up to twice the length of the original one

# TODO
'''

from collections import deque
class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[-1 for _ in range(len(nums))]
        stack=deque()
        # stack the index from left most on top
        for index in range(len(nums)):
            stack.appendleft(index)
            
        start_index=len(nums)-1
        while start_index>=0:
            next_greater_index=stack[len(stack)-1]
            while(nums[start_index] >= nums[next_greater_index] and len(stack)!=0):
                next_greater_index = stack.pop()
            if len(stack)!=0:
                result[start_index]=nums[next_greater_index]
                stack.append(next_greater_index)
            stack.append(start_index)
            start_index-=1
        return result

if __name__=='__main__':
    solution = Solution()
    t1=[1,2,1]
    # expected: [2,-1,2]
    print(solution.nextGreaterElements(t1))
    t2=[1,2,3,4,3]
    # expected: [2,3,4,-1,4]
    print(solution.nextGreaterElements(t2))
    t3=[5,4,3,2,1]
    # expected: [-1,5,5,5,5]
    print(solution.nextGreaterElements(t3))
