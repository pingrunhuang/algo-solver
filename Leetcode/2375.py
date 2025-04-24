"""
Construct Smallest Number From DI String

given a pattern, try to assemble a new string with digit from 1-9 with the following behaviour of a pattern:
D, means decrease
I, means increase

time complexity: O(n^2)
idea: iterate and check
"""
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        i = 0
        result = ""
        numbers = [str(x) for x in range(1,n+2)]
        while i < n:
            count_d = 0
            j=i
            print(i)
            while j < n and pattern[j] == "D":
                count_d+=1
                j+=1
            print(numbers, i, j, count_d)
            if count_d!=0:
                result+="".join(numbers[count_d:0:-1])
                del numbers[count_d:0:-1]
                i=j
            else:
                result+=numbers.pop(0)
                i+=1
            print(result)
        result += numbers.pop(0)
        return result