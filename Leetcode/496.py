class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result=[]
        for x in nums1:
            temp_index = nums2.index(x)
            temp_length = len(result)
            for y in nums2[temp_index:]:
                if y>x:
                    result.append(y)
                    break
            if temp_length==len(result):
                result.append(-1)
        return result
        


if __name__=='__main__':
    solution = Solution()
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    print(solution.nextGreaterElement(nums1,nums2))
    nums1 = [2,4]
    nums2 = [1,2,3,4]
    print(solution.nextGreaterElement(nums1,nums2))


