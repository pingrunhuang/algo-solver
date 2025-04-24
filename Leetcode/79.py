'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
'''

class Solution:
    def dfs(self, i, j, board, word, word_index):
        # the word is consumed which means we have passed the false test
        if word_index==len(word):
            return True
        # make sure we are still in the board and current char is equal to current cell
        if i<0 or i>len(board)-1 or j<0 or j>len(board[0])-1 or board[i][j]!=word[word_index]:
            return False

        tmp = board[i][j]
        board[i][j]="#" # visited
        # check different direction
        result = self.dfs(i-1, j, board, word, word_index+1) or self.dfs(i+1, j, board, word, word_index+1) or self.dfs(i, j-1, board, word, word_index+1) or self.dfs(i, j+1, board, word, word_index+1)
        board[i][j] = tmp
        return result

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if self.dfs(row, col, board, word, 0): return True
        return False



if __name__ == "__main__":
    s = Solution()
    board =[
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    assert s.exist(board, 'A') == True
    assert s.exist(board,'ABCCED')==True
    assert s.exist(board,'ABCCEC')==False
    assert s.exist(board, 'SEE')==True
    assert s.exist(board, 'ABCB')==False
        