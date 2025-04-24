# find the single number in the double list

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.s5(nums)

    def s1(self, nums):
        return 2*sum(set(nums))-sum(nums)

    def s2(self, nums):
        dic = {}
        for i in nums:
            dic[i]=dic.get(i, 0)+1
        for i in dic:
            if dic[i]==1:
                return i

    def s3(self, nums):
        '''
        xor: if x==y, return 0, if 0^=y, return y
        xor is suitable for comparing the 0 and other integer 
        '''
        from functools import reduce
        from operator import xor
        return reduce(xor, nums)

    def s4(self, nums):
        from functools import reduce
        return reduce(lambda x,y:x^y,nums)
    
    def s5(self, nums):
        res = 0
        for i in nums:
            res^=i
        return res
        
if __name__== "__main__":
    solution = Solution()
    t1=[1, 1, 2, 3,3,4,4]
    print(solution.singleNumber(t1))
        