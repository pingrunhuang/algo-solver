class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        memo={}
        for i,v in enumerate(nums):
            if memo.get(v) is None:
                memo[v]=1
            else:
                memo[v]+=1
        result=[]
        for i in memo:
            if memo[i]==2:
                result.append(i)
        return result

        

if __name__=='__main__':
    solution = Solution()
    t1=[4,3,2,7,8,2,3,1]
    print(solution.findDuplicates(t1))