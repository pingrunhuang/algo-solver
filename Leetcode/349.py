'''
349. Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
'''

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = set()
        for n1 in nums1:
            if n1 in nums2:
                result.add(n1)
        return list(result)
        

if __name__ == "__main__":
    solution = Solution()
    t1 = [1, 2, 2, 1]
    t2 = [2,2]
    print(solution.intersection(t1,t2))
