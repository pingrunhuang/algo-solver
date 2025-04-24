'''
leetcode 553: optimal division
Description:
Given a list of positive integers, the adjacent integers will perform the float division. For example, [2,3,4] -> 2 / 3 / 4.

However, you can add any number of parenthesis at any position to change the priority of operations. 
You should find out how to add parenthesis to get the maximum result, and return the corresponding expression in string format.
Your expression should NOT contain redundant parenthesis.

Example:
Input: [1000,100,10,2]
Output: "1000/(100/10/2)"
Explanation:
1000/(100/10/2) = 1000/((100/10)/2) = 200
However, the bold parenthesis in "1000/((100/10)/2)" are redundant, 
since they don't influence the operation priority. So you should return "1000/(100/10/2)". 

Other cases:
1000/(100/10)/2 = 50
1000/(100/(10/2)) = 50
1000/100/10/2 = 0.5
1000/100/(10/2) = 2
Note:
1. The length of the input array is [1, 10].
2. Elements in the given array will be in range [2, 1000].
3. There is only one optimal division for each test case.
'''
import sys

class Division:
    def __init__(self):
        self.max_value = 0
        self.min_value = 1001
        self.max_str = ""
        self.min_str = ""
class Solution:
    def bruteForce(self, start, end, nums, res):
        """
        suppose we split the list into 2 parts by i 
        result = left.max / right.min
        min = left.min / right.max
        """
        
        division = Division()
        if start == end:
            division.max_value = nums[start]
            division.min_value = nums[start]
            division.max_str = str(nums[start])
            division.min_str = str(nums[start])
            return division
        for i in range(start, end):
            left = self.bruteForce(start, i, nums, "")
            right = self.bruteForce(i+1, end, nums, "")
            if left.max_value / right.min_value > division.max_value:
                division.max_value = left.max_value / right.min_value 
                division.max_str = left.max_str + "/" +  ("(" + right.min_str + ")" if i+1==end else right.min_str)
            if left.min_value / right.max_value < division.min_value:
                division.min_value = left.min_value / right.max_value
                division.min_str = left.min_str + "/" + ("(" + right.max_str + ")" if i+1==end else right.max_str)
        return division

    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums)==0:
            return ""
        if len(nums)==1:
            return str(nums[0])
        if len(nums)==2:
            return str(nums[0]) + "/" + str(nums[1])
        return self.bruteForce(0,len(nums)-1, nums, "").max_str
        
class Solution2:
    '''
    let x[0]/x[1]/x[2]... to get the maximum, which is always equal to x[0]/x[1] * (the rest)
    which turns out to be that the rest should get the max. Therefore, it is always x[0]/(x[1]/...)
    '''

    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums)==1:
            return str(nums[0])
        if len(nums)==2:
            return str(nums[0]) + "/" + str(nums[1])
        result = str(nums[0])+"/(" +str(nums[1])
        for i in range(2,len(nums)):
            result += "/" + str(nums[i])
        return result+")"

if __name__ == "__main__":
    test1 = [1000, 100, 10, 2]
    solution = Solution()
    print(solution.optimalDivision(test1))
