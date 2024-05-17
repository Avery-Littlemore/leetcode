# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
 
# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

class Solution:
    def subsets(self, nums):
        def backtrack(start_idx, candidates, candidate, results):
            results.append(candidate.copy())
        
            for idx in range(start_idx, len(candidates)): # if you need the index use `enumerate`
                # if True:  # replace True with the dead-end condition
                #     continue
            
                candidate.append(candidates[idx])  # take
                backtrack(idx + 1, candidates, candidate, results)  # explore
                candidate.pop()  # clean up
        results = []
        candidate = []
        backtrack(0, nums, candidate, results)
        return results
    
class Solution:
    def subsets(self, nums):
        
        def backtrack(candidates, candidate, results, start):
            if len(candidate) == len(candidates):
                return

            
            for idx in range(start, len(candidates)):
                current_num = candidates[idx]
                candidate.append(current_num)

                results.append(candidate)
                backtrack(candidates, candidate, results, idx + 1)
                candidate.pop()
        
        candidate = []
        results = [[]]

        backtrack(nums, candidate, results, 0)
        return results