class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        nums=sorted(nums)
        for i,v in enumerate(nums):
            if i%2==0:
                result+=v
        return result

if __name__=='__main__':
    solution = Solution()
    test_case1= [1,123,2,5]
    result1=solution.arrayPairSum(test_case1)
    print(result1)