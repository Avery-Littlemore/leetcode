# You are given an m x n grid where each cell can have one of three values:
    # 0 representing an empty cell,
    # 1 representing a fresh orange, or
    # 2 representing a rotten orange.

# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# Example 1:
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Example 2:
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

# Example 3:
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        queue = []
        fresh_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                    
                if grid[r][c] == 2:
                    queue.append((r, c))
        
        minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue and fresh_count:
            curr_length = len(queue)
            for _ in range(curr_length):
                row, col = queue.pop(0)
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        fresh_count -= 1
                        queue.append((new_row, new_col))

            minutes += 1
                

        if fresh_count > 0:
            return -1
        return minutes
        