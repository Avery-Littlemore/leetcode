# Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

# The value of |x| is defined as:
# x if x >= 0.
# -x if x < 0.

# Example 1:
# Input: nums = [1,2,2,1], k = 1
# Output: 4
# Explanation: The pairs with an absolute difference of 1 are:
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]

# Example 2:
# Input: nums = [1,3], k = 3
# Output: 0
# Explanation: There are no pairs with an absolute difference of 3.

# Example 3:
# Input: nums = [3,2,1,5,4], k = 2
# Output: 3
# Explanation: The pairs with an absolute difference of 2 are:
# - [3,2,1,5,4]
# - [3,2,1,5,4]
# - [3,2,1,5,4]
 
# Constraints:
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
# 1 <= k <= 99

"""
P:
- Take as in put an array of integers
- take as input a number k
- Return the number of permutations in which the absolute value of one element minus the absolute value of a second element equals the value of k
- nums are all pos

E:
Input: nums = [1,2,2,1], k = 1
Output: 4

Input: nums = [1,3], k = 3
Output: 0

Input: nums = [3,2,1,5,4], k = 2
Output: 3

D:
consider only array for now
need to read through once at least... aim for O(N) time complexity
O(N) space complexity if I use a hash for speedy read. Maybe O(1) is possible?

A:
- create variable total and set to 0
- iterate through the list 
    - add each num as a key to a dict with truthy value of 1
    - if it exists on multiple occasions, +1 each time
- iterate again
    - check if current number plus k exists
        - add 1 * the value (aka, num of occurrences) of that key

"""

class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        total = 0
        hash_table = {}

        for num in nums:
            if hash_table.get(num):
                hash_table[num] += 1
            else:
                hash_table[num] = 1
            
        for num in nums:
            if hash_table.get(k + num):
                total += hash_table[k + num]

        return total