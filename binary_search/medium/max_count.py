# Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers 
# and the number of negative integers.

# In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, 
# then return the maximum of pos and neg.

# Note that 0 is neither positive nor negative.

# Example 1:
# Input: nums = [-2,-1,-1,1,2,3]
# Output: 3
# Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.

# Example 2:
# Input: nums = [-3,-2,-1,0,0,1,2]
# Output: 3
# Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.

# Example 3:
# Input: nums = [5,20,66,1314]
# Output: 4
# Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.
 
# Constraints:
# 1 <= nums.length <= 2000
# -2000 <= nums[i] <= 2000
# nums is sorted in a non-decreasing order.

"""
P:
- take an array of numbers as input
- numbers are in ascending order
    - repeats are allowed
- count the number of negative numbers and the number of positive numbers
    - return the number of occurrences which is the higher of the two

- zero does not count for either
- repeated numbers are still counted

- find the lowest pos num
- find the highest neg num

E:
Input: nums = [-2,-1,-1,1,2,3]
Output: 3

Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3

Input: nums = [5,20,66,1314]
Output: 4

Input: nums = [0,0]
Output: 0

D:
- Take an array (list) as input
- read through once only
- aim for O(logN) time comp and O(1) space comp

A:
- set pivot index at (integer) half the length of the array
- set upper limit to the last index in the array
- set lower limit to the first index in the array
- set lowest_pos_idx to undefined
- set highest_neg_idx to undefined
- find the lowest pos num loop
    - if pivot is less than or equal 0
        - set lower limit to pivot
    - if pivot is positive
        - set lowest_pos_idx to current index
        - set upper limit to pivot
    - set pivot to mid-point between lower and upper limits
    - break if upper limit - lower limit == 1
- set pivot to midway between upper_limit and 0
- set lower_limit to 0
- find the highest neg num loop
    - if pivot is greater than or equal 0
        - set upper limit to pivot
    - if pivot is negative
        - set highest_neg_idx to current index
        - set lower limit to pivot
    - set pivot to mid-point between upper and lower limits
    - break if upper limit - lower limit == 1
- if lowest pos idx exists
    - pos_nums = list length - lowest pos idx
- else
    - pos_nums = 0
- if highest neg idx exists
    - neg_nums = highest neg idx + 1
- else
    - neg_nums = 0
- return the higher of the two nums

"""

class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pivot_idx = len(nums) // 2
        upper_limit = len(nums) - 1
        lower_limit = 0
        
        lowest_pos_idx = None
        highest_neg_idx = None

        while True:
            if nums[pivot_idx] > 0:
                lowest_pos_idx = pivot_idx
                upper_limit = pivot_idx
            else:
                lower_limit = pivot_idx
            
            if upper_limit == lower_limit:
                break
            elif (upper_limit - lower_limit) == 1:
                if pivot_idx == upper_limit:
                    pivot_idx = lower_limit
                    upper_limit = lower_limit
                else:
                    pivot_idx = upper_limit
                    lower_limit = upper_limit
            else:
                pivot_idx = upper_limit - (upper_limit - lower_limit) // 2

        pivot_idx = upper_limit // 2
        lower_limit = 0

        while True:
            if nums[pivot_idx] < 0:
                highest_neg_idx = pivot_idx
                lower_limit = pivot_idx
            else:
                upper_limit = pivot_idx
            
            if upper_limit == lower_limit:
                break
            elif (upper_limit - lower_limit) == 1:
                if pivot_idx == upper_limit:
                    pivot_idx = lower_limit
                    upper_limit = lower_limit
                else:
                    pivot_idx = upper_limit
                    lower_limit = upper_limit
            else:
                pivot_idx = upper_limit - (upper_limit - lower_limit) // 2

        if lowest_pos_idx or lowest_pos_idx == 0:
            pos_nums = len(nums) - lowest_pos_idx
        else:
            pos_nums = 0
        
        if highest_neg_idx or highest_neg_idx == 0:
            neg_nums = highest_neg_idx + 1
        else:
            neg_nums = 0

        return max(pos_nums, neg_nums)