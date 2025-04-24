'''
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
'''
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])
        row_check   = [{} for _ in range(rows)]
        col_check   = [{} for _ in range(cols)]
        grid_check  = [[{} for _ in range(3)] for _ in range(3)]
        
        for row in range(rows):
            for col in range(cols):
                cur_val = board[row][col]
                if cur_val == '.':
                    continue
                cur_grid_row = row//3
                cur_grid_col = col//3
                if row_check[row].get(cur_val) or col_check[col].get(cur_val) or grid_check[cur_grid_row][cur_grid_col].get(cur_val):
                    return False
                else:
                    row_check[row].update({cur_val:True})
                    col_check[col].update({cur_val:True})
                    grid_check[cur_grid_row][cur_grid_col].update({cur_val:True})
        return True



if __name__ == "__main__":
    s = Solution()
    t1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert s.isValidSudoku(t1)==True

    t2 = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert s.isValidSudoku(t2)==False

