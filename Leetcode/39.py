'''
TODO: search for more efficient solution
'''
class Solution:
    def dfs(self, candidates, acceptable_set, target, result, begin_index):
        if target == 0:
            result.append(acceptable_set.copy())
            # mark this backtrack trace is ok
            return True
        if target<0:
            # mark this backtrack trace is not ok
            return False
        for i in range(begin_index, len(candidates)):
            value = candidates[i]
            acceptable_set.append(value)
            self.dfs(candidates, acceptable_set, target-value, result, i)
            acceptable_set.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(sorted(candidates), [], target, result, 0)
        return result

if __name__ == "__main__":
    s = Solution()
    t1 = [2,3,6,7]
    print(s.combinationSum(t1, 7))
    t2 = [2,3,5]
    print(s.combinationSum(t2, 8))
    t3 = [7,3,2]
    print(s.combinationSum(t3, 18)) # [[2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,3,3],[2,2,2,2,3,7],[2,2,2,3,3,3,3],[2,2,7,7],[2,3,3,3,7],[3,3,3,3,3,3]]