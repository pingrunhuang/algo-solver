#!/bin/python

'''
Utilized a concept of stack
'''

class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        round_points=[0,0]
        for op in ops:
            if op == 'C':
                round_points.pop()
            elif op=='+':
                # notice how to get the last 2 value 
                round_points.append(round_points[-1]+round_points[-2])
            elif op=='D':
                round_points.append(2*round_points[-1])
            else:
                round_points.append(int(op))
                
        return sum(round_points)
        

if __name__ == "__main__":
    solution = Solution()
    testCase1=["5","2","C","D","+"]
    print(solution.calPoints(testCase1))
    testCase2=["5","-2","4","C","D","9","+","+"]
    print(solution.calPoints(testCase2))