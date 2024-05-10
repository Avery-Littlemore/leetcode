# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1

# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
 
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        anchor = 0
        runner = 0
        total = nums[runner]
        lowest_found = None

        while runner < len(nums) and anchor < len(nums):
            if total >= target:
                if not lowest_found:
                    lowest_found = runner - anchor + 1
                elif runner - anchor + 1 < lowest_found:
                    lowest_found = runner - anchor + 1
                total -= nums[anchor]
                anchor += 1
            else:
                runner += 1
                if runner >= len(nums):
                    break
                total += nums[runner]

        if not lowest_found:
            return 0
        else:
            return lowest_found