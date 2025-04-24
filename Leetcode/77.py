'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

permutation and Combination
'''

class Solution:
    def rec(self, result, combination, start_index, nums, k):
        if k==0:
            result.append(combination.copy())
        else:
            for num in nums[start_index:]:
                combination.append(num)
                start_index=num
                self.rec(result, combination, start_index, nums, k-1)
                combination.pop()

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n:
            return []
        result = []
        self.rec(result, [], 0, range(1, n+1), k)
        return result



if __name__ == "__main__":
    s = Solution()
    print(s.combine(4, 2))
    print(s.combine(3,3))