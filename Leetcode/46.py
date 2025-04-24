'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

'''

class Solution(object):
    def dfs(self, result, nums, temp_result):
        """
        @param result List(List())
        @param nums 
        """
        if len(nums) == len(temp_result):
            result.append(temp_result.copy())
            return
        else:
            for num in nums:
                if num in temp_result: 
                    continue
                temp_result.append(num)
                self.dfs(result, nums, temp_result)
                temp_result.pop()

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(result, nums, [])
        return result

if __name__ == '__main__':
    s = Solution()
    t1 = [1,2,3]
    s.permute(t1) #[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    t2 = [0,1]
    s.permute(t2) #[[0,1],[1,0]]
