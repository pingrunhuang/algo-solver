from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_store = {}
        result = []
        for i in range(len(nums)):
            if nums[i] in diff_store:
                diff = nums[i]
                return [diff_store[diff], i]
            else:
                diff = target-nums[i]
                diff_store[diff] = i
                
        return result