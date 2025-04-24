'''
This is a generalization of solving the n sum problem

In this scenario, I will use recursion and dp memoization for solving this problem.

Questions to ask:
1. has duplicates element or not?
2. sorted or not?
'''

class Solution:
    def __init__(self):
        self.final_result = []

    def findNsum_recursive(self, nums, target, N, temp_result=[]):
        '''
        sorted_nums: a list of sorted number
        target: the target number to be sum
        temp_result: the result list for recording the current level corresponding to the different N 
        '''
        nums.sort()
        if len(nums)<N or N<2:
            return
        if N==2:
            left = 0
            right = len(nums)-1
            while left<right:
                if nums[left]+nums[right]==target:
                    self.final_result.append(temp_result+[nums[left], nums[right]])
                    # either case, you'd have to move the pointer first
                    left+=1
                    right-=1
                    # skip the duplicated num: since I have checked it in the recursion part, therefore it is unnecessary for skipping here
                    # but due to explanation, I still keep it here 
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right -=1 
                elif nums[left]+nums[right]<target:
                    left+=1
                else:
                    right-=1
        else:
            for i in range(len(nums)-N+1):
                # sorted list
                if target<nums[i]*N or target>nums[-1]*N:
                    break
                if i==0 or (i>0 and nums[i]!=nums[i-1]):
                    self.findNsum_recursive(nums[i+1:],target-nums[i], N-1, temp_result=temp_result+[nums[i]])
        return


if __name__=="__main__":
    s = Solution()
    t1 = [-3,-2,-1,0,0,1,2,3]
    s.findNsum_recursive(t1, 0, N=4)
    print(s.final_result)