'''
Given an array of penny size and an aim target to be changed, calculate the number of ways changement

Summary:
From this solution, we can see that the recursion method actually apply to the situation where only 2 possibilities for each step
Like the fibanacci.
'''

class Solution():
    def calculateWaysWithMemoize(self, arr, aim):
        pass

    def calculateWaysWithRecursion(self, arr, aim):
        if len(arr)==0 or aim<0:
            return 0
        elif aim==0:
            return 1
        else:
            return self.calculateWaysWithRecursion(arr[1:], aim) + self.calculateWaysWithRecursion(arr, aim-arr[0])


if __name__=='__main__':
    size_arr = [1,5,10,20]
    solution = Solution()
    print(solution.calculateWaysWithRecursion(size_arr, 6))
