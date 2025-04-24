'''

Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.
'''

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums)==0:
            return 0
        n = len(nums)
        nums.sort()
        p1 = 0
        p2 = 0
        while p1 < n:
            if nums[p1] != val:
                nums[p2] = nums[p1]
                p2+=1
            else:
                nums[p2]=nums[p1]
            p1+=1
        nums = nums[:p2]
        return p2

if __name__ == "__main__":
    solution = Solution()
    t1 = [3,2,2,3,5]
    s1 = 3
    result1 = solution.removeElement(t1, s1)
    print(result1)
    for i in t1:
        print(i, end="\t")
    
