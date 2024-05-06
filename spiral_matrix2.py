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
        path = 'right'
        while len(result) < total_matrix_size:            
            result.append(matrix[row][column])
            if path == 'right':
                if column < len(matrix[row]) - spiral_number:
                    column += 1
                else:
                    row += 1
                    path = 'down'
            elif path == 'down':
                if row < len(matrix) - spiral_number:
                    row += 1
                else:
                    column -= 1
                    path = 'left'
            elif path == 'left':
                if column > spiral_number - 1:
                    column -= 1
                else:
                    row -= 1
                    path = 'up'
            elif path == 'up':
                if row > spiral_number:
                    row -= 1
                else:
                    column += 1
                    spiral_number += 1
                    path = 'right'
            
        return result