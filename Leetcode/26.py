'''
26. Remove Duplicates from Sorted Array


Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

2 pointers
'''

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==0:
            return 0

        p1=0
        p2=0
        while p1 < n-1:
            if nums[p1]!=nums[p1+1]:
                p2+=1
                nums[p2]=nums[p1+1]
            p1+=1
        del nums[p2+1:]
        return p2+1


if __name__ == "__main__":
    solution = Solution()
    t1 = [1,1,2,2,2,3,3,4]
    print(solution.removeDuplicates(t1))
    print(t1)