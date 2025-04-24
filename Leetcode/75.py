'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.
'''


class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        two pass
        """
        num_zero = 0
        num_one = 0
        num_two = 0
        for num in nums:
            if num==0:
                num_zero+=1
            elif num==1:num_one+=1
            else:num_two+=1
        for i in range(num_zero):
            nums[i]=0
        for i in range(num_zero, num_zero + num_one):
            nums[i]=1
        for i in range(num_zero + num_one, num_zero + num_one+num_two):
            nums[i]=2

class Solution2:
    def sortColors(self, nums):
        """
        one-pass algorithm using only constant space
        """
        # TODO


if __name__ == "__main__":
    s = Solution()
    t = [2,0,2,1,1,0]
    s.sortColors(t)
    print(t)
        