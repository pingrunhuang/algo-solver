'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
1. The number of elements initialized in nums1 and nums2 are m and n respectively.
2. You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
'''

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        i = 0
        while i < m+n and j<n:
            if nums1[i]>nums2[j]:
                for rest in range(m+n-1, i-1, -1):
                    nums1[rest] = nums1[rest-1]
                nums1[i]=nums2[j]
                j+=1
            i+=1
        rest_start = m+j
        for i in range(rest_start,m+n):
            nums1[i]=nums2[j]
            j+=1




if __name__ == "__main__":
    s = Solution()
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    m=3
    n=3
    s.merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [2,0]
    m = 1
    nums2 = [1]
    n = 1
    s.merge(nums1, m, nums2, n)
    print(nums1)

    