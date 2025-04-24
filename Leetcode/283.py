'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        lastNonZeroElementIndex = 0
        for i in range(n):
            if nums[i]!=0:
                nums[lastNonZeroElementIndex] = nums[i]
                lastNonZeroElementIndex+=1
        for i in range(lastNonZeroElementIndex, n):
            nums[i]=0
        print(nums)    
        

if __name__ == "__main__":
    solution = Solution()
    t1 = [0, 1, 0, 3, 12]
    solution.moveZeroes(t1)
    t2=[0,0,1]
    solution.moveZeroes(t2)
