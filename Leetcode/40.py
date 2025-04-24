'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
'''

class Solution:
    def dfs(self, sorted_candidates, acceptable_set, result, target, start, occurence_map):
        if target==0:
            if not occurence_map.get(''.join([str(x) for x in acceptable_set])):
                occurence_map.update({''.join([str(x) for x in acceptable_set]):True})
                result.append(acceptable_set.copy())
            return
        elif target<0:
            return
        else:
            for i in range(start, len(sorted_candidates)):
                acceptable_set.append(sorted_candidates[i])
                self.dfs(sorted_candidates, acceptable_set, result, target-sorted_candidates[i], i+1, occurence_map)
                acceptable_set.pop()

    def dfs_solver(self, candidates, target):
        result = []
        occurence_map = {}
        self.dfs(sorted(candidates), [], result, target, 0, occurence_map)
        return result

    def dp_solver(self, candidates, target):
        candidates.sort()
        # dp的每一个元素是个set，每个set里面记录达成i总和的时候可行的组合
        dp = [set() for _ in range(target+1)]
        dp[0].add(()) # different from set(())
        for num in candidates:
            for pre_target in range(target, num-1, -1):
                print(pre_target)
                for combination in dp[pre_target-num]:
                    # TypeError: can only concatenate tuple (not "int") to tuple (without the comma)
                    # tuple is not modifiable, adding a new tuple to a set is using set + (b,) syntax
                    dp[pre_target].add(combination+(num,))
        return list(list(x) for x in dp[-1])

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.dp_solver(candidates, target)




if __name__=='__main__':
    s=Solution()
    # t1 = [10,1,2,7,6,1,5]
    # print(s.combinationSum2(t1, 8))
    # t2 = [2,5,2,1,2]
    # print(s.combinationSum2(t2, 5))
    t3 = [1,3,4,7]
    print(s.combinationSum2(t3, 8))
