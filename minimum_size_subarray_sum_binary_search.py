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

def sumFound(target, nums, window):
    left = 0
    right = window - 1
    sum = 0

    for i in range(window):
        sum += nums[i]

    if sum >= target: return True

    while right < len(nums) - 1:
        sum -= nums[left]
        left += 1
        right += 1
        sum += nums[right]
        if sum >= target: return True
    
    return False

def minSubArrayLen(target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    ceil = len(nums)
    floor = 1

    found = False
    min_subarray_size = 0

    while True:
        window = (ceil + floor) // 2

        found = sumFound(target, nums, window)
        if found: min_subarray_size = window

        if ceil == floor:
            break
        elif found:
            ceil = window
        else:
            floor = window + 1

        found = False
        
    return min_subarray_size
            
 
class Solution(object):
    def sumFound(self, target, nums, window):
        left = 0
        right = window - 1
        sum = 0

        for i in range(window):
            sum += nums[i]

        if sum >= target: return True

        while right < len(nums) - 1:
            sum -= nums[left]
            left += 1
            right += 1
            sum += nums[right]
            if sum >= target: return True
        
        return False

    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        ceil = len(nums)
        floor = 1

        found = False
        min_subarray_size = 0

        while True:
            window = (ceil + floor) // 2

            found = self.sumFound(target, nums, window)
            if found: min_subarray_size = window

            if ceil == floor:
                break
            elif found:
                ceil = window
            else:
                floor = window + 1

            found = False
            
        return min_subarray_size

print(minSubArrayLen(7, [2,3,1,2,4,3]))
print(minSubArrayLen(4, [1,4,4]))
print(minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
# print(minSubArrayLen())
      