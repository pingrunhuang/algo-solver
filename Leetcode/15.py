class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []
        target = 0 
        result = []
        nums = sorted(nums)
        print(nums)
        for index in range(len(nums)-2):
            # could not have duplicate triplet
            if index>0 and nums[index-1]==nums[index]:
                continue

            left,right = index+1, len(nums)-1
            while left<right:
                if nums[left]+nums[right]+nums[index]==target:
                    result.append([nums[index],nums[left],nums[right]])
                    left+=1
                    right-=1
                    # could not have duplicate triplet
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif nums[left]+nums[right]+nums[index]<target:
                    left+=1
                else:
                    right-=1
        return result

if __name__ == '__main__':
    s = Solution()
    t1 = [-1, 0, 1, 2, -1, -4] 
    e1 = [[-1, 0, 1],[-1, -1, 2]]
    print(s.threeSum(t1))