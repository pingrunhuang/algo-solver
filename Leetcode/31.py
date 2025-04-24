'''
Find the next greater permutation 

a list of integers will have many different permutation. our mission is to modify the current permutation, so that it is just larger then the current permutation

核心思想：找出一个刚刚好比当前的数大的数
hard part:
1. 为什么要从右往左（反之会找到远大于当前值的数）
2. 当找到第一个相邻的降序对nums[i], nums[i-1]的时候，怎么用O(N)的时间在nums[i:]里找到那个刚好比nums[i-1]大的数

permutation and Combination
'''

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # the list is already is the largest permutation, therefore return the smallest permutation
        if sorted(nums, reverse=True) == nums:
            nums.sort()
            return
        len_nums = len(nums)
        ascending_queue = []
        for i in range(len_nums-1, 0, -1):
            ascending_queue.append(nums[i])
            if nums[i]>nums[i-1]:
                index = i
                for j in range(len_nums-i):
                    cur_temp_item = ascending_queue.pop(0)
                    if cur_temp_item > nums[i-1]:
                        ascending_queue.insert(0, nums[i-1])
                        nums[i-1] = cur_temp_item
                        index = i + j
                        break
                    else:
                        nums[i+j] = cur_temp_item
                len_rest_ascending_queue = len(ascending_queue)
                for j in range(len_rest_ascending_queue):
                    nums[index+j]=ascending_queue.pop(0)
                # print(nums)
                return
        

if __name__ == "__main__":
    s = Solution()
    t1 = [1,2,5,8,7,6]
    print("Original: ", t1)
    s.nextPermutation(t1)
    t2 = [2,3,1]
    print("Orifinal: ", t2)
    s.nextPermutation(t2)
    t3 = [3,2,1]
    print("Original: ", t3)
    s.nextPermutation(t3)