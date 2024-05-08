# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line 
# are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# i.e., 7 (num of continuous i) x 7 (highest "bookend" elements)

# Example 2:
# Input: height = [1,1]
# Output: 1

# [1,4,3,3, 3,9]
#  0 1 2 3  4 5  6  7
# [5,7,3,10,2,99,1,54]

# [1,3,4,2,1]
# [4,3,1,2,4]

"""
volume = (anchor - runner) * min(height[anchor], height[runner])

"""





# def calculate_area(x1, x2, y1, y2):
#     x_axis = x2 - x1
#     y_axis = min(y1, y2)
    
#     return x_axis * y_axis

# def max_area(height):
#     start = 0
#     end = len(height) - 1
#     current_max_area = calculate_area(start, end, height[0], height[len(height) - 1])
    
#     while start < end:
#         current_area = calculate_area(start, end, height[start], height[end])

#         if current_area > current_max_area:
#             current_max_area = current_area
            
#         if height[start] < height[end]:
#             start += 1
#         else:
#             end -= 1
            
#     return current_max_area