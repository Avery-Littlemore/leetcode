# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Constraints:
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 
# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as 
# extra space for space complexity analysis.)

"""
P:
- Take array of numbers as input
- The output should be an array of the same size
- each element of the output array should be the result of the product of every OTHER indexed element in the input array
- no division allowed
- try for O(1) space complexity

E:
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

D:
Input: array of numbers
Output: array of numbers


A:
- set prev product = 1
- set product_array = []
- iterate through the array
    - set current element to the product of the remaining elements of the array


"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        right_products = [1] * len(nums)
        next_product = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            [next_product, right_products[i]] = [nums[i] * next_product, next_product]
            i -= 1

        prev_product = 1
        for i in range(len(nums)):
            [prev_product, nums[i]] = [nums[i] * prev_product, prev_product * right_products[i]]

        return nums
