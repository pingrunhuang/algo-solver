'''
TODO
'''
class Solution:
#     def backtrack(self, nums, result, prev_set, level):
#         if level==len(nums):
#             temp_set = set()
#             for num in nums:
#                 for perm in result:
#                     pass

#             result.append(temp_set)
#             return
#         else:
#             for i in range(current_index, len(nums)):
#                 temp_set += (nums[i],)
#                 self.backtrack(nums, result, temp_set, i+1)
#                 temp_set=temp_set[:-1]
#                 print()

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
#         result = []
#         self.backtrack(nums, result, (), 0)
#         print(result)
#         return result

if __name__ == "__main__":
    s = Solution()
    t1 = [1,1,2]
    s.permuteUnique(t1)