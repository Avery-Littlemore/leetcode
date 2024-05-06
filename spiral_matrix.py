# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

"""
P:
Input: array consisting of nested arrays, N x M (not necessarily equal)
Output: (flattened) array of elements in spiral order
- Take an array consisting of subarrays
- Each subarray is a row of a matrix
    - subarrays will be of the same size
- create a new array which will consist of the spiral order of the array matrix
    - spiral order traverses the top row, then the right side, then the bottom row, then the left side, etc
    - once an element is traversed, it cannot be touched again
    - ends when all elements have been found (aka, output array has the same number of elements as the flattened input array)

Implicit:
- The first row (subarray) will always be the first N digits

E:
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
[1,  2,  3,  4 ]
[5,  6,  7,  8 ]
[9,  10, 11, 12]

Example 3:
Input:
columns0   1   2
row 0 [1,  2,  3 ]
row 1 [4,  5,  6 ]
row 2 [7,  8,  9 ]
row 3 [10, 11, 12]


**empty matrices**


D:
- Use lists for both

A:
- Create an empty result array
- create a total_matrix_size = array length * subarray length
- set row = 0
- set column = 0
- spiral_number = 1
- while result array size < total_matrix_size
    - while true 
        - if result array size == total_matrix_size
            - break
        - insert into result the element at row, column 
        - if column is less than the subarray length - spiral_number
            - iterate column by 1
        - else
            - iterate row by 1
            - break
    - while true 
        - if result array size == total_matrix_size
            - break
        - insert into result the element at row, column 
        - if row is less than to array length - spiral_number
            - iterate row by 1
        - else
            - de-iterate column by 1
            - break
    - while true
        - if result array size == total_matrix_size
            - break
        - insert into result the element at row, column 
        - if column is greater than spiral_number - 1
            - de-iterate column by 1
        - else
            - de-iterate row by 1
            - break
    - while true
        - if result array size == total_matrix_size
            - break
        - insert into result the element at row, column 
        - if row is greater than spiral_number
            - de-iterate row by 1
        - else
            - iterate column by 1
            - break
    - iterate spiral_number

- return result array


- 

C:
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        result = []
        total_matrix_size = len(matrix) * len(matrix[0])
        row = 0
        column = 0
        spiral_number = 1
        while len(result) < total_matrix_size:            
            while len(result) < total_matrix_size:
                result.append(matrix[row][column])
                if column < len(matrix[row]) - spiral_number:
                    column += 1
                else:
                    row += 1
                    break

            while len(result) < total_matrix_size:
                result.append(matrix[row][column])
                if row < len(matrix) - spiral_number:
                    row += 1
                else:
                    column -= 1
                    break

            while len(result) < total_matrix_size:
                result.append(matrix[row][column])
                if column > spiral_number - 1:
                    column -= 1
                else:
                    row -= 1
                    break

            while len(result) < total_matrix_size:
                result.append(matrix[row][column])
                if row > spiral_number:
                    row -= 1
                else:
                    column += 1
                    break
            
            spiral_number += 1
            
        return result