'''
55. Jump Game

Good interviewing process from simple to complex but efficient.
'''

class Solution:
    def rec(self, nums, cur_pos, dp):
        if cur_pos + nums[cur_pos]>len(nums)-1:
            return True
        if not dp[cur_pos]:
            return False
        for step in range(1, nums[cur_pos]+1):
            if self.rec(nums, cur_pos+step, dp):
                return True
            else:
                dp[cur_pos+step]=False
        return False

    def my_recursive_solution(self, nums):
        """
        Time limit exceed!
        """
        dp = [True for _ in range(len(nums))]
        result = self.rec(nums,0, dp)
        return result

    
    def bottomUpDP(self, nums):
        self.status = {"unknown":-1, "bad":0, "good":1}



    def loopSolution(self, nums):
        """
        Actually for each position, I just need to check if I can reach the position from the previous position. And whether this is true depends on the maximum step that I can jump in the previous position.O(n) time complexity.
        """
        previous_furthest_reachable_index = 0
        for current_position, maximum_step in enumerate(nums):
            if previous_furthest_reachable_index < current_position:
                return False
            previous_furthest_reachable_index = max(previous_furthest_reachable_index, current_position+maximum_step)
        return True 
    
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.loopSolution(nums)


if __name__ == "__main__":
    s = Solution()
    t1 = [2,3,1,1,4]
    assert s.canJump(t1)
    t2 = [3,2,1,0,4]
    assert not s.canJump(t2)
    t3 = [3,0,8,2,0,0,1]
    assert s.canJump(t3)
    t4 = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    assert not s.canJump(t4)