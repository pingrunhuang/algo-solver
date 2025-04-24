
'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:

    You must not modify the array (assume the array is read only).
    You must use only constant, O(1) extra space.
    Your runtime complexity should be less than O(n2).
    There is only one duplicate number in the array, but it could be repeated more than once.



2 primitive solution:
    1. sort
    2. set
'''

class Solution:

    def findDuplicate(self, nums):
        '''
        assuming n is the length  of the nums
        time complexity: O(n)
        '''
        if len(nums) > 1:
            # find the entry of the cycle
            slow = nums[0]
            fast = nums[nums[0]]
            while slow!=fast:
                slow = nums[slow]
                # fast pointer fun 2 steps a time
                fast = nums[nums[fast]]
            fast = 0
            while slow!=fast:
                fast = nums[fast]
                slow = nums[slow]
            return fast
        



    def findDuplicate2(self, nums):
        """
        this will not assume the n is the length of the array
        time complexity: O(nlogn)
        :type nums: List[int]
        :rtype: int
        """
        # this fast slow method is suitable for traverse through the whole list 
        n = len(nums)
        fast = 0
        slow = 0
        count = 1
        while True:
            if nums[slow] == nums[fast] and slow!=fast:
                break

                   
            print(slow, fast)    
            if fast==n-1:
                fast=0
            if slow==n-1:
                slow=0
            if count%2==0:
                slow+=1
            fast+=1
            count+=1 

        print(slow, fast)
        return nums[slow]

if __name__ == "__main__":
    solution = Solution()
    t1 = [4,1,5,4,2,4]
    print(solution.findDuplicate(t1))
    t2 = [1,2,2]
    print(solution.findDuplicate(t2))
    t3 = [1,1]
    print(solution.findDuplicate(t3))
    t4=[1,3,4,2,1]
    print(solution.findDuplicate(t4))