'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Permutation and combination
'''

class Solution:
    def dfs(self, result, combination, nums, start_index, depth):
        if depth==0:
            result.append(combination.copy())
        else:
            for num in nums[start_index:]:
                combination.append(num)
                # TODO: Why do I need to reset the start_index here insdead of placing start_index+1
                start_index = start_index+1
                self.dfs(result, combination, nums, start_index, depth-1)
                combination.pop()


    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for k in range(len(nums)+1):
            self.dfs(result, [], nums, 0, k)
        return result
    

if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1,2,3]))
    print(s.subsets([3,9]))
        