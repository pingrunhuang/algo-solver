'''
6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''
from queue import Queue
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s)==1 or numRows==1:
            return s
        is_going_down = False
        current_row = 0
        rows = ['' for _ in range(numRows)]
        for v in s:
            rows[current_row]+=v
            is_going_down = not is_going_down if current_row==0 or current_row==numRows-1 else is_going_down
            current_row = current_row + 1 if is_going_down else current_row - 1
        return ''.join(rows)

    
if __name__ == "__main__":
    solution = Solution()
    t1 = "PAYPALISHIRING"
    n1 = 3
    e1 = "PAHNAPLSIIGYIR"
    print(solution.convert(t1, n1))