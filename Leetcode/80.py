'''
80. Remove Duplicates from Sorted Array II

Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # TODO
        pass
        
class Solution2:
    def removeDuplicates(self, nums):
        '''
        Incredible solution from https://leetcode.com/stefanpochmann
        '''
        i = 0
        AT_MOST = 2
        for num in nums:
            if i<AT_MOST or num > nums[i-AT_MOST]:
                nums[i]=num
                i+=1
        print(nums)
        return i

if __name__ == "__main__":
    s = Solution()
    t1 = [1,1,1,2,2,3]
    assert s.removeDuplicates(t1)==5
    t2 = [0,0,1,1,1,1,2,3,3]
    assert s.removeDuplicates(t2)==7
    t3 = [1,1,2,3,4,5,5,5,5,5,5,5,5]
    assert s.removeDuplicates(t3)==7