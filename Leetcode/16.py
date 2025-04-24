'''
Transformation of two pointers 


Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


TODO
'''

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-1):
            left, right = i+1, len(nums)-1
            while left<right:
                temp_sum = nums[i] + nums[left] + nums[right]
                if temp_sum==target:
                    return target
                if abs(target-temp_sum)<abs(target-result):
                    result = temp_sum

                if temp_sum<target:
                    left+=1
                if temp_sum>target:
                    right-=1
        return result


if __name__ == "__main__":
    solution = Solution()
    s1=[-1,2,1,-4]
    target1=1
    print(solution.threeSumClosest(s1, target1))

    s2=[0,2,1,-3]
    target2=1
    print(solution.threeSumClosest(s2, target2))

    s3=[1,2,5,10,11]
    target3=12
    print(solution.threeSumClosest(s3, target3))