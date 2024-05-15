# You are given an integer array nums. You are initially positioned at the array's first index, 
# and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

"""
2 3 1 1 4
        

3 2 1 0 4


5 0 0 0 0 1


"""

# class Solution(object):
#     def canJump(self, nums):
#         cache = {}
#         def helper(idx):
#             if idx >= len(nums) - 1:
#                 return True
#             if nums[idx] == 0:
#                 return False
            
#             for jump in range(nums[idx], 0, -1):
#                 if idx + jump in cache:
#                     return cache[idx + jump]
#                 else:
#                     cache[idx + jump] = helper(idx + jump)
#                     if cache[idx + jump]:
#                         return True

#             return False

#         return helper(0)
    
# Greedy Algo
class Solution(object):
    def canJump(self, nums):
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False
            # update the farthest
            farthest = max(farthest, nums[i] + i)
            if farthest >= len(nums) - 1:
                return True
            
        return False