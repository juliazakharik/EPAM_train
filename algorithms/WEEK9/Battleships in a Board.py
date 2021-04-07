"""
419. Battleships in a Board
Medium
Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.

"""

# Runtime: 60 ms, faster than 46.22% of Python online submissions for Battleships in a Board.
# Memory Usage: 16.6 MB, less than 98.32% of Python online submissions for Battleships in a Board.
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        res = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    if i == len(board) - 1 or board[i + 1][j] == '.':
                        if j == len(board[i]) - 1 or board[i][j + 1] == '.': 
                            res += 1
        return res