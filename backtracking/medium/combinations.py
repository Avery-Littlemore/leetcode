# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.

# Example 1:
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

# Example 2:
# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination. 

# Constraints:
# 1 <= n <= 20
# 1 <= k <= n

class Solution(object):
    def combine(self, max_num, size_of_subarr):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(current_num, candidate, results):
            if len(candidate) == size_of_subarr:
                results.append(candidate.copy())
                return
        
            for i in range(1 + current_num, max_num + 1): # if you need the index use `enumerate`
                # if True:  # replace True with the dead-end condition
                #     continue
            
                candidate.append(i)  # take
                backtrack(i, candidate, results)  # explore
                candidate.pop()  # clean up
        results = []
        candidate = []
        backtrack(0, candidate, results)
        return results