"""
Mine sweaper

TODO
"""

class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        row = click[0]
        col = click[1]
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board
        

if __name__ == '__main__':
    solution = Solution()
    test_case1=[
        ['E', 'E', 'E', 'E', 'E'],
        ['E', 'E', 'M', 'E', 'E'],
        ['E', 'E', 'E', 'E', 'E'],
        ['E', 'E', 'E', 'E', 'E']
        ]

    test_case2=[
        ['B', '1', 'E', '1', 'B'],
        ['B', '1', 'M', '1', 'B'],
        ['B', '1', '1', '1', 'B'],
        ['B', 'B', 'B', 'B', 'B']
        ]

    result1=solution.updateBoard(test_case1, [3,0])
    result2=solution.updateBoard(test_case2, [1,2])
    print(result1)
    print(result2)