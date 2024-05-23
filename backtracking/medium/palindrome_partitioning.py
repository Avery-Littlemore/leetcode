# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:
# Input: s = "a"
# Output: [["a"]]

# Constraints:
# 1 <= s.length <= 16
# s contains only lowercase English letters.

class Solution:
    def partition(self, s):
        def is_palindrome(substr):
            return substr == substr[::-1]

        def backtrack(s, candidate, results):
            if len(s) == 0:
                results.append(candidate.copy())
                return
        
            for idx in range(len(s)): # if you need the index use `enumerate`
                substring = s[0:idx + 1]
                
                if is_palindrome(substring):
                    candidate.append(substring)  # take
                    backtrack(s[idx + 1:], candidate, results)  # explore
                    candidate.pop()  # clean up
        results = []
        candidate = []
        backtrack(s, candidate, results)
        return results