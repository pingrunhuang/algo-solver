'''
Two pointers
'''

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        left_pointer = 0
        right_pointer = len(height)-1
        while left_pointer<right_pointer:
            if result<(right_pointer-left_pointer)*min(height[left_pointer],height[right_pointer]):
                result = (right_pointer-left_pointer)*min(height[left_pointer],height[right_pointer])
                
            if height[left_pointer]>height[right_pointer]:
                right_pointer-=1
            else:
                left_pointer+=1
        
        return result
                


if __name__ == "__main__":
    solution = Solution()
    t1 = [1,2,3,4,5,67,8]
    print(solution.maxArea(t1))