# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example 1:
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

# Example 2:
# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 200

class Solution(object):
    
    def helper(self, grid, row, col, memo):
        if row < 0 or col < 0:
            return float('inf')
        
        if row == 0 and col == 0:
            return grid[row][col]

        if (row, col) not in memo:
            top = self.helper(grid, row - 1, col, memo)
            left = self.helper(grid, row, col - 1, memo)
            memo[(row, col)] = min(left, top) + grid[row][col]

        return memo[(row, col)]


    def minPathSum(self, grid):
        """[]
        :type grid: List[List[int]]
        :rtype: int
        """
        
        return self.helper(grid, len(grid) - 1, len(grid[0]) - 1)
    

# Try to solve it in O(1) space complexity...
# class Solution(object):
#     def minPathSum(self, grid):
#         def helper(row, col):
#             if row < 0 or col < 0:
#                 return float('inf')
            
#             if row == 0 and col == 0:
#                 return grid[row][col]

#             top = helper(row - 1, col)
#             left = helper(row, col - 1)
#             return min(left, top) + grid[row][col]

#             # return grid[row][col]
        
#         return helper(len(grid) - 1, len(grid[0]) - 1)