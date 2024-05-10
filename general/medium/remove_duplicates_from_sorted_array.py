# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
# The remaining elements of nums are not important as well as the size of nums.
# Return k.

# Custom Judge:
# The judge will test your solution with the following code:
"""
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
"""
# If all assertions pass, then your solution will be accepted.

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Constraints:
# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.

"""
O(N) time complexity is minimum. Aiming for that...

P:
Input: list of integers in ascending order (not necessarily consecutive)
Output: return number of unique values in list -> k
    Implicit: mutated list with first k elements comprising the in-order unique values in the list

- Take a list of integers
- discern how many are unique
- mutate the list to push all the unique values to the front of the array
- return the number of unique integers found
- remaining values in the array are irelevant

E: 
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

Input: nums = [0,0,3,5]
Output: 5, nums = [0,3,5,0]

D:
List (array) to be mutated
Potentially use a hash table for quick read capabilities

A:
- Take list as input
- Create an empty hash table (dict)
- iterate through list
    - if element does not exist as a key
        - mutate the element at position [length of hash table]
        - add element as a key with truthy value True
        

"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hash_table = {}
        
        for num in nums:
            if not hash_table.get(num):
                nums[len(hash_table)] = num
                hash_table[num] = True
        
        return len(hash_table)

# O(N) space complexity... could actually do it in O(1) with clever solution copied below
# class Solution:
#     def removeDuplicates(self, nums):
#         n = len(nums)
#         if n < 2:
#             return n
#         ans, j = 1, 0
#         for i in range(1, n):
#             if nums[i] != nums[j]:
#                 j += 1
#                 nums[j] = nums[i]
#                 ans += 1
#         return ans