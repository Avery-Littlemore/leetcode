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

"""
P:
- take an array with nested arrays as input, and a target number
- return true if the target number exists in any of the arrays

- each array is in ascending order
- the highest num in the previous array will be lower than the lowest num in the next array

E:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

D:
- Aim for O(log (N * M)) time comp, where n and m are the array indices 
    - i.e., binary search

A:
- take the middlemost sublist as our pivot
- check if the target is lower than the first element
    - if so, set pivot as the sublist between the first sublist and the current pivot
- check if the target is higher than the last element
    - if so, set pivot as the sublist between the last sublist and the current pivot
- if neither,
    - set the middlemost element as the pivot
    - set the upper_limit as the final element
    - set the lower_limit as the first element
    - while lower_limit does not equal the upper limit
        - if the target is above the pivot
            - set the lower_limit to the pivot
            - set the pivot as the element between the pivot and the upper_limit
        - else if the target is below the pivot
            - set the upper_limit to the pivot
            - set the pivot as the element between the pivot and the lower_limit
        - else if the target is the pivot
            - return true
- return false


"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        upper_index = len(matrix)
        lower_index = 0
        pivot_index = upper_index // 2
        prev_pivot = None

        while pivot_index != prev_pivot:
            if len(matrix) == pivot_index or pivot_index < 0:
                return False
            elif matrix[pivot_index][0] > target:
                upper_index = pivot_index
            elif matrix[pivot_index][-1] < target:
                lower_index = pivot_index
            else:
                break

            index_shift = (upper_index - lower_index) // 2 if upper_index - lower_index > 1 else 1
            prev_pivot = pivot_index
            pivot_index = upper_index - index_shift

        target_row = matrix[pivot_index]
        upper_index = len(target_row)
        lower_index = 0
        pivot_index = upper_index // 2
        prev_pivot = None

        while pivot_index != prev_pivot:
            if target_row[pivot_index] > target:
                upper_index = pivot_index
            elif target_row[pivot_index] < target:
                lower_index = pivot_index
            else:
                return True
            
            index_shift = (upper_index - lower_index) // 2 if upper_index - lower_index > 1 else 1
            prev_pivot = pivot_index
            pivot_index = upper_index - index_shift
        
        return False


def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    
    upper_index = len(matrix)
    lower_index = 0
    pivot_index = upper_index // 2
    prev_pivot = None

    while pivot_index != prev_pivot:
        if len(matrix) == pivot_index or pivot_index < 0:
            return False
        elif matrix[pivot_index][0] > target:
            upper_index = pivot_index
        elif matrix[pivot_index][-1] < target:
            lower_index = pivot_index
        else:
            break

        index_shift = (upper_index - lower_index) // 2 if upper_index - lower_index > 1 else 1
        prev_pivot = pivot_index
        pivot_index = upper_index - index_shift

    target_row = matrix[pivot_index]
    upper_index = len(target_row)
    lower_index = 0
    pivot_index = upper_index // 2
    prev_pivot = None

    while pivot_index != prev_pivot:
        if target_row[pivot_index] > target:
            upper_index = pivot_index
        elif target_row[pivot_index] < target:
            lower_index = pivot_index
        else:
            return True
        
        index_shift = (upper_index - lower_index) // 2 if upper_index - lower_index > 1 else 1
        prev_pivot = pivot_index
        pivot_index = upper_index - index_shift
    
    return False


print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

print(searchMatrix([[1]], 0))
print(searchMatrix([[1]], 2))