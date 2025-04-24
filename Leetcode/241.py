
class Solution:
    def __init__(self):
        self.dp = {}

    def operation(self, a, b, opt):
        if opt=='+':
            return a+b
        elif opt=='-':
            return a-b
        elif opt=='*':
            return a*b
        
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        result = []
        if input.isdigit():
            return [int(input)]

        for i, v in enumerate(input):
            if v == '+' or v == '-' or v == '*':
                result_left = self.diffWaysToCompute(input[:i])
                result_right = self.diffWaysToCompute(input[i+1:])
                for x1 in result_left:
                    for x2 in result_right:
                        result.append(self.operation(x1, x2, v))
        return result
    
    def diffWaysToComputeDP(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if self.dp.get(input) is not None:
            return self.dp.get(input)
        if input.isdigit():
            return [int(input)]
        result = []
        for i, v in enumerate(input):
            if v in "+-*":
                left_result = self.diffWaysToComputeDP(input[:i])
                right_result = self.diffWaysToComputeDP(input[i+1:])
                for x1 in left_result:
                    for x2 in right_result:
                        result.append(self.operation(x1,x2,v))
                self.dp[input]=result
        return result
        
         
        

if __name__=='__main__':
    solution = Solution()
    testCase1 = "2-1-1"
    testCase2 = "2*3-4*5"
    print(solution.diffWaysToComputeDP(testCase1))
    print(solution.diffWaysToComputeDP(testCase2))