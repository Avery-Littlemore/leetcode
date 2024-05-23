# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:
# Input: nums = [1]
# Output: [[1]]

# Constraints:
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.

class Solution:
    def permute(self, nums):
        def backtrack(candidates, candidate, results):
            if len(candidate) == len(candidates):
                results.append(candidate.copy())
                return
        
            for elem in candidates: # if you need the index use `enumerate`
                if elem in candidate:  # replace True with the dead-end condition
                    continue
            
                candidate.append(elem)  # take
                backtrack(candidates, candidate, results)  # explore
                candidate.pop()  # clean up
        results = []
        candidate = []
        backtrack(nums, candidate, results)
        return results

# def some_problem(candidates):
#     def backtrack(candidates, candidate, results):
#         if "<<success condition>>":
#             results.append(candidate.copy())
#             return
    
#         for elem in candidates: # if you need the index use `enumerate`
#             if True:  # replace True with the dead-end condition
#                 continue
        
#             candidate.append(elem)  # take
#             backtrack(candidates, candidate, results)  # explore
#             candidate.pop()  # clean up
#     results = []
#     candidate = []
#     backtrack(candidates, candidate, results)
#     return results

# print(some_problem([1, 2, 3]))
