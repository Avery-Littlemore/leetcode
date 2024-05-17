# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example 1:
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.

# Example 2:
# Input: board = [["X"]]
# Output: [["X"]]

# Constraints:
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def mark_island(row, col):
            if row < 0 or col < 0 or row == rows or col == cols or board[row][col] != 'O':
                return
            
            board[row][col] = 'V'
            mark_island(row, col - 1)
            mark_island(row - 1, col)
            mark_island(row, col + 1)
            mark_island(row + 1, col)


        for r in range(rows):
            if board[r][0] == 'O':
                mark_island(r, 0)
            if board[r][cols - 1] == 'O':
                mark_island(r, cols - 1)

        for c in range(cols):
            if board[0][c] == 'O':
                mark_island(0, c)
            if board[rows - 1][c] == 'O':
                mark_island(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'V':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
        
