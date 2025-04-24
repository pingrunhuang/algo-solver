''' Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships. '''


class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board:
            return 0
        rows = len(board)
        cols = len(board[0])
        count = 0
        for x in range(rows):
            for y in range(cols):
                if board[x][y]=='X' and (x==0 or board[x-1][y]=='.') and (y==0 or board[x][y-1]=='.'):
                    count+=1
        return count


        

if __name__=='__main__':
    testcase1=[['X','.','.','X'],
                ['.','.','.','X'],
                ['.','.','.','X']]

    solution = Solution()
    print(solution.countBattleships(testcase1))