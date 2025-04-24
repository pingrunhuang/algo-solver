'''
350. Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:
- What if the given array is already sorted? How would you optimize your algorithm?
    use two pointers
- What if nums1's size is small compared to nums2's size? Which algorithm is better?
    I think the first one is better since we can always check for the shorter one in each iteration
- What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
    get part of the elements from nums2 for one time and repeat untill nums2 is all checked. The goal is to reduce the disk IO


other solution like distributed system: 
    1. store on dfs and use map reduce paradigm
    2. use spark streaming
'''
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result=[]
        for i in nums1:
            if i in nums2:
                result.append(i)
                # because element should be appeared in both arrays
                nums2.remove(i)
        return result

    def intersect_sorted(self, nums1, nums2):
        '''
        nums1 and nums2 are sorted ascending 
        '''
        result = []
        n1 = len(nums1)
        n2 = len(nums2)
        p1 = 0
        p2 = 0
        while p1<n1 and p2<n2:
                if nums1[p1]>nums2[p2]:
                    p2+=1
                elif nums1[p1]<nums2[p2]:
                    p1+=1
                else:
                    result.append(nums1[p1])
                    p1+=1
                    p2+=1
        return result

            
if __name__ == "__main__":
    solution = Solution()
    n1 = [1,2,2,1]
    n2 = [2,2]
    print(solution.intersect(n1, n2))
    n3 = [1,2,2,1]
    n4 = [2]
    print(solution.intersect(n3,n4))
    n5 = [1,1,2,2]
    n6 = [1,2]
    print(solution.intersect_sorted(n5, n6))

