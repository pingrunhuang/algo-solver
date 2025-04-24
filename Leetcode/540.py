

class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        distinct_vals = set(nums)
        return sum(distinct_vals)*2-total
        


if __name__=='__main__':
    solution = Solution()
    t1=[3,3,7,7,10,11,11]
    print(solution.singleNonDuplicate(t1))
    t2=[1,1,2,3,3,4,4,8,8]
    print(solution.singleNonDuplicate(t2))
