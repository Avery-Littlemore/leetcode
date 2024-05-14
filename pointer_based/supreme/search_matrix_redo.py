# You are given an m x n integer matrix `matrix` with the following two properties:
    # Each row is sorted in non-decreasing order.
    # The first integer of each row is greater than the last integer of the previous row.

# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.

# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4

class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        
        row_min = 0
        row_max = len(matrix) - 1

        while row_min <= row_max:
            row_mid = (row_min + row_max) // 2

            if matrix[row_mid][0] > target:
                row_max = row_mid - 1
            elif matrix[row_mid][-1] < target:
                row_min = row_mid + 1
            else:
                break

        col_min = 0
        col_max = len(matrix[row_mid]) - 1

        while col_min <= col_max:
            col_mid = (col_min + col_max) // 2

            if matrix[row_mid][col_mid] > target:
                col_max = col_mid - 1
            elif matrix[row_mid][col_mid] < target:
                col_min = col_mid + 1
            else:
                return True

        return False

