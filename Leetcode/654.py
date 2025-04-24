
'''
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
    The root is the maximum number in the array.
    The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
    The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.

'''

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==0:
            return 
        if  len(nums) == 1:
            return TreeNode(nums[0])
        maxValueIndex = 0
        maxValue = nums[maxValueIndex]
        for i,v in enumerate(nums):
            if v>maxValue:
                maxValueIndex=i
                maxValue=v
        leftTree = self.constructMaximumBinaryTree(nums[0:maxValueIndex])
        rightTree = self.constructMaximumBinaryTree(nums[maxValueIndex+1:len(nums)])
        result = TreeNode(maxValue)
        result.left=leftTree
        result.right=rightTree
        return result

    def bfs(self, root):
        from collections import deque
        queue = deque()
        if root==None:
            return
        queue.append(root)
        while len(queue)!=0:
            current_node = queue.popleft()
            if current_node.left!=None:
                queue.append(current_node.left)
            if current_node.right!=None:
                queue.append(current_node.right)
            print(str(current_node.val)+ '->', end=' ')


if __name__ == '__main__':
    test_case1 = [3,2,1,6,0,5]
    
    solution = Solution()
    result1 = solution.constructMaximumBinaryTree(test_case1)
    print(solution.bfs(result1))
